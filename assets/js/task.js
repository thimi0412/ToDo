let colortCnt = 0;
$(function () {
    const inputLimit = new Date($('.input-limit').val());

    // modal
    $(document).on('click', '.open-options', function (event) {
        event.preventDefault();
        $('#modal-options').iziModal('open');
        $('.input-limit').val(getDate());
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
        const inputLimit = new Date($('.input-limit').val());
        const nowDate = new Date(getNow());

        const a = getDate(getNow(inputLimit))
        console.log(a)

        if (inputLimit.getTime() > nowDate.getTime()
            || getDate(getNow(inputLimit)) === getDate(getNow(nowDate))) {
            $('.task-list').append(
                `<li class='task'>
            <div class="task-text">
                <p class="task-info">${inputTask}</p>
                <p class="into-limit">期限 : ${getDate(getNow(inputLimit))}</p>
            </div>
            <div class="task-btn">
                <p class="into-date">追加日 : ${getNow()}</p>
                <button class="del-btn">削除</button>
                <button class="edit-task">色変更</button>
            </div>
            </li>`
            );
            $('#modal-options').iziModal('close');
            $('.input-task').val('');
        } else {
            alert('期限日より前です');
            $('#modal-options').iziModal('close');
        }
    });

    // タスク削除処理
    $('.task-list').on('click', '.del-btn', (evt) => {
        const isDelete = confirm('タスクを削除しますか？');
        if (isDelete) {
            $(evt.currentTarget).parent().parent()
                .fadeOut(1000, () => {
                    $(evt.currentTarget).parent().parent().remove();
            });
        }
    });

    // タスク更新処理
    $('.task-list').on('click', '.edit-task', (evt) => {
        const isEdit = confirm('タスクを編集しますか？');
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
 * 現在時刻を返す(yyyy/mm/dd HH:MM:ss)
 * @returns {string} text
 */
function getNow(now = new Date()) {
    year = now.getFullYear();
    month = toDD(now.getMonth() + 1);
    date = toDD(now.getDate());
    hour = toDD(now.getHours());
    min = toDD(now.getMinutes());
    sec = toDD(now.getSeconds());
    let text = year + '/' + month + '/' + date + ' '
        + hour + ':' + min + ':' + sec;
    return text;
}

/**
 * 現在日付を取得(yyyy/mm/dd)
 * @returns {string} text
 */
function getDate(now = getNow()) {
    var date = now.split(' ')[0];
    const dateArray = date.split('/');
    const yyyymmdd = `${dateArray[0]}-${dateArray[1]}-${dateArray[2]}`;

    return yyyymmdd;
}