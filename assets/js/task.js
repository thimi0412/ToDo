let colortCnt = 0;
$(function () {
    $(document).on('click', '.open-options', function (event) {
        event.preventDefault();
        $('#modal-options').iziModal('open');
    });
    $('#modal-options').iziModal({
        headerColor: '#26A69A', //ヘッダー部分の色
        width: 1000, //横幅
        heigth: 5000,
        overlayColor: 'rgba(0, 0, 0, 0.5)', //モーダルの背景色
        transitionIn: 'fadeInUp', //表示される時のアニメーション
        transitionOut: 'fadeOutDown' //非表示になる時のアニメーション
    });

    // タスク追加
    $('.add-btn').on('click', (evt) => {
        const inputTask = $('.input-task').val();
        $('.task-list').append(
            `<li class='task'>${getDate()} <br>
            <p class="task-info">${inputTask}</p>
            <div class="task-btn">
            <button class="del-btn">削除</button>
            <button class="edit-task">色変更</button>
            </div>
            </li>`
        );
        $('#modal-options').iziModal('close');
        $('.input-task').val('');
    })

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
 * 現在時刻を返す(yyyy/mm/dd/ HH:MM:ss)
 * @returns {string} text
 */
function getDate() {
    const now = new Date();
    year = now.getFullYear();
    month = toDD(now.getMonth());
    date = toDD(now.getDate());
    hour = toDD(now.getHours());
    min = toDD(now.getMinutes());
    sec = toDD(now.getSeconds());
    let text = year + '/' + month + '/' + date + ' '
        + hour + ':' + min + ':' + sec;
    return text;
}