let colortCnt = 0;
$(function () {
    // ajax通信開始
    $.ajax({
        type: "GET",
        url: "http://localhost:8080/get",
        dataType: "json",
    }).done(function (res) {
        for (let i of res.result) {
            // すでに存在するタスクを追加
            $('.task-list').append(
                `<li class='task'>
                    <div class="task-text">
                        <p class="task-info">${i.title}</p>
                        <p class="task-info-main">${i.details}</p>
                        <p class="into-limit">期限 : ${i.limit}</p>
                    </div>
                    <div class="task-btn">
                        <p class="into-date">追加日 : ${i.insert}</p>
                        <button class="del-btn">削除</button>
                        <button class="edit-task">変更</button>
                    </div>
                </li>`
            );
        }
    }).fail(function (res) {
        console.log(res)
    });

    const inputLimit = new Date($('.input-limit').val());


    // タスク追加のmodal
    $(document).on('click', '.open-options', function (event) {
        event.preventDefault();
        $('#modal-options').iziModal('open');

        $('.input-limit').val(getNow());
    });
    $('#modal-options').iziModal({
        headerColor: '#26A69A', //ヘッダー部分の色
        width: 1000, //横幅
        padding: 50,
        overlayColor: 'rgba(0, 0, 0, 0.5)', //モーダルの背景色
        transitionIn: 'fadeInUp', //表示される時のアニメーション
        transitionOut: 'fadeOutDown' //非表示になる時のアニメーション
    });
    // タスク追加
    $('.add-btn').on('click', () => {
        const inputTask = $('.input-task').val();
        const inputTaskMain = $('.input-task-main').val();
        const inputLimit = new Date($('.input-limit').val());
        const nowDate = new Date(getNow());

        if (inputLimit.getTime() > nowDate.getTime()
            || getDate(getNow(inputLimit)) === getDate(getNow(nowDate))) {
            $('.task-list').append(
                `<li class='task'>
                    <div class="task-text">
                        <p class="task-info">${inputTask}</p>
                        <p class="task-info-main">${inputTaskMain}</p>
                        <p class="into-limit">期限 : ${
                            trimT(getDate(getNow(inputLimit)))}</p>
                    </div>
                    <div class="task-btn">
                        <p class="into-date">追加日 : ${trimT(getNow())}</p>
                        <button class="del-btn">削除</button>
                        <button class="edit-task">変更</button>
                    </div>
                </li>`
            );

            // リクエストを送るjsonを作成
            reqJson = {
                title: inputTask,
                details: inputTaskMain,
                limit: inputLimit,
                insert: nowDate,
            };
            $.ajax({
                type: "POST",
                url: "http://localhost:8080/set",
                data: reqJson,
                dataType: "json",
            });
            $('#modal-options').iziModal('close');
            $('.input-task').val('');
            $('.input-task-main').val('');
        } else {
            $('#modal-alert').iziModal('open');
            $('#modal-alert').iziModal({
                headerColor: '#d43838',
                width: 400,
                autoOpen: true,
                pauseOnHover: true,
                timeoutProgressbar: true,
                attached: 'bottom'
            });

        }
    });

    // タスクのidを取得
    let taskId;
    $('.task-list').on('click', 'li .edit-task', (evt) => {
        var index = $('li .edit-task').index(evt.currentTarget);
        taskId = index;
    });
    $('.task-list').on('click', 'li .del-btn', (evt) => {
        var index = $('li .del-btn').index(evt.currentTarget);
        taskId = index;
    });


    // タスク更新処理のmodal
    $(document).on('click', '.edit-task', function (event) {
        event.preventDefault();
        $('#modal-options2').iziModal('open');

        // 更新を押したタスクの情報を取得
        const taskList = $('.task-list').children().eq(taskId);
        const editTitel = taskList.find('.task-info').text();
        const editDetails = taskList.find('.task-info-main').text();
        const editLimit = addT(taskList.find('.into-limit').text().split(' '));
        const editInsert = taskList.find('.into-date').text().split(' ');


        // 入力フォームに事前に入れる
        $('.edit-task').val(editTitel);
        $('.edit-task-main').val(editDetails);
        $('.edit-limit').val(editLimit);
    });
    $('#modal-options2').iziModal({
        headerColor: '#26A69A', //ヘッダー部分の色
        width: 1000, //横幅
        padding: 50,
        overlayColor: 'rgba(0, 0, 0, 0.5)', //モーダルの背景色
        transitionIn: 'fadeInUp', //表示される時のアニメーション
        transitionOut: 'fadeOutDown' //非表示になる時のアニメーション
    });
    // タスク更新処理
    $('.edit-btn').on('click', () => {
        const intoEditTitle = $('.edit-main .edit-task').val();
        const intoEditDetails = $('.edit-main .edit-task-main').val();
        const intoEditLimit = $('.edit-main .edit-limit').val();
        const intoEditInsert = new Date(getNow());
        
        // リクエストを送るjsonを作成
        reqJson = {
            title: intoEditTitle,
            details: intoEditDetails,
            limit: intoEditLimit,
            insert: intoEditInsert,
            index : taskId,
        };
        $.ajax({
            type: "POST",
            url: "http://localhost:8080/update",
            data: reqJson,
            dataType: "json",
        });
        const taskList2 = $('.task-list').children().eq(taskId);
        taskList2.find('.task-info').text(intoEditTitle);
        taskList2.find('.task-info-main').text(intoEditDetails);
        taskList2.find('.into-limit').text('期限 : ' + trimT(intoEditLimit));
        $('#modal-options2').iziModal('close');
    });


    //削除modal
    $(document).on('click', '.del-btn', function (event) {
        event.preventDefault();
        $('#modal-del').iziModal('open');
    });
    $('#modal-del').iziModal({
        headerColor: '#26A69A', //ヘッダー部分の色
        width: 1000, //横幅
        padding: 50,
        overlayColor: 'rgba(0, 0, 0, 0.5)', //モーダルの背景色
        transitionIn: 'fadeInUp', //表示される時のアニメーション
        transitionOut: 'fadeOutDown' //非表示になる時のアニメーション
    });
    //削除処理
    $('.del-yes').on('click', (evt) => {
        reqJson = {
            index: taskId,
        };
        $.ajax({
            type: "POST",
            url: "http://localhost:8080/delete",
            data: reqJson,
            dataType: "json",
        });
        $('#modal-del').iziModal('close');

        $('.task-list').children().eq(taskId).remove();

    });
    $('.del-no').on('click', () => {
        $('#modal-del').iziModal('close');
    });
})


/**
 * 日付の0埋め
 * @param {number} num 
 * 
 * @returns {string} num
 */
function toDD(num) {
    num += '';
    if (num.length === 1) {
        num = '0' + num;
    }
    return num;
};

/**
 * 現在時刻を返す(yyyy-mm-dd HH:MM:ss)
 * @returns {string} text
 */
function getNow(now = new Date()) {
    year = now.getFullYear();
    month = toDD(now.getMonth() + 1);
    date = toDD(now.getDate());
    hour = toDD(now.getHours());
    min = toDD(now.getMinutes());
    sec = toDD(now.getSeconds());
    let text = year + '-' + month + '-' + date + 'T'
        + hour + ':' + min + ':' + sec;
    return text;
}

/**
 * 現在日付を取得(yyyy/mm/dd)
 * @returns {string} text
 */
function getDate(now = getNow()) {
    const date = now.split(' ')[0];
    const dateArray = date.split('-');
    const yyyymmdd = `${dateArray[0]}-${dateArray[1]}-${dateArray[2]}`;

    return yyyymmdd;
}


function trimT(dateTime) {
    dateTime = dateTime.split('T');
    return dateTime[0] + ' ' + dateTime[1];
}

function addT(dateTime) {
    return dateTime[2] + 'T' + dateTime[3];
}
