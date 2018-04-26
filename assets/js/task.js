let colortCnt = 0;
const colorList = ['rgb(248, 164, 164)',
                    'rgb(163, 163, 248)',
                    'rgb(250, 250, 124)'];
$(function() {
    $('.add-btn').on('click', () => {
        $('.task-list').append(
            `<li class='task'>${getDate()}
            <button class="del-btn">削除</button>
            <button class="ch-color">色変更</button>
            </li>`
        );
        cnt += 1;
    });

    $('.task-list').on('click', '.del-btn', (evt) => {
        $(evt.currentTarget).parent().remove();
    });

    $('.task-list').on('click', '.ch-color', (evt) => {
        let color = colorList[colortCnt];
        $(evt.currentTarget).parent().css({background: color});
        colortCnt += 1;
        if (colortCnt === colorList.length) {
            colortCnt = 0;
        }
    });
})

function toDD(num) {
    num += '';
    if(num.length === 1) {
        num = '0' + num;
    }
    return num;
};


function getDate() {
    const now = new Date();
    year = now.getFullYear();
    month = toDD(now.getMonth());
    date = toDD(now.getDate())
    hour = toDD(now.getHours());
    min = toDD(now.getMinutes());
    sec = toDD(now.getSeconds());
    let text = year + '/' + month + '/' + date + ' '
                + hour +':'+ min +':'+ sec;
    return text;
}