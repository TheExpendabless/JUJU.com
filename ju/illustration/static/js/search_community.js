
$(document).ready(function(){
    var url = new URL(window.location.href);
    var bizcircle = url.searchParams.get("bizcircle");
    var station = url.searchParams.get("station");
    if (bizcircle) {
        $('#bizcircle').val(bizcircle);
        getcommunitybybizcircle()
    }
    if (station) {
        $('#station').val(station);
        getcommunitybystation()
    }
    $("#navdistrict li").click(function(){
         var district = $(this).text();
         var bizcircle;
         if(district=='浦东'){
             bizcircle=['万祥镇','川沙','临港新城','周浦','惠南','高行','外高桥','世博','曹路','三林','金杨','祝桥','书院镇','大团镇','塘桥',
                   '潍坊','唐镇','北蔡','泥城镇','航头','康桥','洋泾','源深','高东','宣桥','新场','金桥','南码头','合庆','张江','御桥','陆家嘴',
                   '杨东','碧云','花木','老港镇','联洋'];
         }
         else if(district=='杨浦'){
             bizcircle=['控江路','五角场', '周家嘴路', '中原', '新江湾城', '黄兴公园', '鞍山', '东外滩'];
         }
         else if(district=='虹口'){
             bizcircle=['四川北路', '北外滩', '临平路', '鲁迅公园', '江湾镇', '凉城', '曲阳'];
         }
         else if(district=='青浦'){
             bizcircle=['夏阳', '徐泾', '白鹤', '赵巷', '华新', '盈浦', '练塘','香花桥', '朱家角', '重固', '金泽'];
         }
         else  if(district=='闸北'){
             bizcircle=['彭浦', '西藏北路', '闸北公园', '阳城', '不夜城', '大宁', '永和'];
         }
         else if(district=='奉贤'){
             bizcircle=['南桥', '海湾', '西渡', '奉贤金汇', '奉城', '青村', '柘林', '庄行', '四团'];
         }
         else if(district=='金山'){
             bizcircle=['张堰', '石化', '枫泾', '金山', '朱泾', '亭林', '山阳','漕泾', '廊下', '吕巷'];
         }
         else if(district=='宝山'){
             bizcircle=['罗店', '月浦', '淞宝', '顾村', '大华', '上大', '高境', '张庙', '通河', '大场镇', '共富', '淞南', '杨行', '共康', '罗泾'];
         }
         else if(district=='闵行'){
             bizcircle=['颛桥', '古美', '浦江','七宝','吴泾','华漕','航华','老闵行','金虹桥','莘庄','龙柏','梅陇','春申','金汇','静安新城','马桥'];
         }
         else  if(district=='嘉定'){
             bizcircle=['外冈', '新成路', '菊园新区', '马陆', '嘉定老城', '江桥', '嘉定新城', '南翔', '丰庄', '安亭', '徐行', '华亭', '上大'];
         }
         else if(district=='长宁'){
             bizcircle=['中山公园', '北新泾', '虹桥', '新华路', '天山', '镇宁路', '古北', '西郊', '仙霞'];
         }
         else if(district=='松江'){
             bizcircle=['松江老城', '九亭', '松江新城', '松江大学城', '泗泾', '新桥', '佘山', '车墩', '石湖荡', '莘闵别墅', '小昆山', '叶榭', '新浜', '泖港'];
         }
         else if (district=='徐汇'){
             bizcircle=['衡山路', '斜土路', '万体馆', '建国西路', '徐家汇', '龙华', '长桥', '上海南', '康健', '田林', '华东理工', '漕河泾', '华泾', '植物园', '徐汇滨江'];
         }
         else if (district=='黄浦'){
             bizcircle=['南京东路', '五里桥', '董家渡', '打浦桥', '蓬莱公园', '新天地', '淮海中路', '人民广场', '豫园', '老西门', '世博滨江', '黄浦滨江'];
         }
         else if(district=='普陀'){
             bizcircle=['甘泉宜川', '长寿路', '桃浦', '光新', '长征', '真如', '武宁', '长风', '真光', '曹杨', '中远两湾城', '万里'];
         }
         else {
             bizcircle=['昆山', '太仓', '嘉兴', '苏州', '海门', '启东', '上海周边', '南通'];
         }
         $('#nav1').empty();
         $.each(bizcircle, function(i, item) {
                    $('#nav1').append("<li role=\"presentation\"><a href=\"?bizcircle="+item+"\">" + item + "</a></li>");
                });
         $('#navdistrict li').removeClass('active');
         $(this).addClass('active');
    })
    $("#navsub li").click(function(){
         var line = $(this).text();
         var stations;
         if(line=='1号线'){
             stations=['共康路', '延长路', '陕西南路', '徐家汇', '黄陂南路', '上海火车','上海马戏城', '常熟路','莘庄', '通河新村', '汉中路',
                        '中山北路', '上海南站', '汶水路', '呼兰路', '共富新村','彭浦新村','衡山路', '漕宝路', '人民广场', '宝安公路',
                        '新闸路', '锦江乐园', '外环路', '上海体育馆', '莲花路', '富锦路', '友谊西路'];
         }
         else if(line=='2号线'){
             stations=['川沙', '南京西路', '南京东路', '北新泾','华夏东路', '世纪大道', '娄山关路', '中山公园', '陆家嘴', '江苏路',
                        '唐镇', '虹桥火车站', '广兰路', '创新中路', '世纪公园', '威宁路', '淞虹路', '龙阳路', '静安寺', '金科路',
                        '徐泾东', '张江高科', '上海科技馆', '东昌路'];
         }
         else if(line=='3号线'){
             stations=['淞滨路', '龙漕路', '东宝兴路', '宝山路', '延安西路', '虹口足球场', '江湾镇', '大柏树', '虹桥路', '中潭路',
                        '江杨北路', '镇坪路', '赤峰路', '友谊路', '金沙江路', '殷高西路', '宝杨路', '宜山路', '曹杨路', '石龙路',
                        '长江南路', '张华浜', '水产路', '淞发路', '铁力路', '漕溪路'];
         }
         else if(line=='4号线'){
             stations=['西藏南路', '大木桥路', '鲁班路', '海伦路', '东安路', '临平路', '蓝村路', '浦电路', '浦东大道', '上海体育场',
                        '大连路', '塘桥', '南浦大桥', '杨树浦路'];
         }
         else if(line=='5号线'){
             stations=['颛桥', '北桥', '华宁路', '剑川路', '金平路', '东川路', '闵行开发区', '春申路', '银都路', '文井路'];
         }
         else  if(line=='6号线'){
             stations=['源深体育中心', '灵岩南路', '高青路', '博兴路', '东明路', '港城路', '金桥路', '巨峰路', '上南路', '临沂新村',
                        '高科西路', '洲海路', '华夏西路', '民生路', '外高桥保税区北', '云山路', '东方体育中心', '航津路', '上海儿童医学中心',
                        '德平路', '五莲路', '东靖路', '北洋泾路', '五洲大道', '外高桥保税区南'];
         }
         else if(line=='7号线'){
             stations=['肇嘉浜路', '龙华中路', '耀华路', '刘行', '大华三路', '芳华路', '行知路', '罗南新村', '场中路', '岚皋路', '长寿路',
                        '杨高南路', '大场镇', '美兰湖', '昌平路', '新村路', '花木路', '长清路', '上海大学', '锦绣路', '云台路', '顾村公园',
                        '南陈路', '上大路', '后滩', '潘广路'];
         }
         else if(line=='8号线'){
             stations=['延吉中路', '江浦路', '曲阜路', '西藏北路', '陆家浜路', '市光路', '老西门', '杨思', '翔殷路', '黄兴公园', '芦恒路', '曲阳路',
                        '鞍山新村', '中兴路', '黄兴路', '嫩江路', '四平路', '凌兆新村', '联航路', '江月路', '浦江镇',
                        '大世界', '成山路'];
         }
         else if(line=='9号线'){
             stations=['小南门', '打浦桥', '松江新城', '马当路', '泗泾', '嘉善路', '醉白池', '松江体育中心', '松江大学城', '佘山',
                        '洞泾', '七宝', '桂林路', '九亭', '中春路', '星中路', '合川路', '漕河泾开发区', '杨高中路', '商城路'];
         }
         else if(line=='10号线'){
             stations=['国权路', '上海图书馆', '天潼路', '四川北路', '交通大学', '三门路', '殷高东路', '豫园', '伊犁路', '上海动物园',
                        '水城路', '邮电新村', '龙柏新村', '江湾体育场', '紫藤路', '虹桥1号航楼', '同济大学', '五角场', '新江湾城',
                        '新天地', '航中路', '龙溪路', '宋园路'];
         }
         else if(line=='11号线'){
             stations=['嘉定西', '三林', '嘉定北', '三林东', '隆德路', '李子园', '兆丰路', '上海西站', '南翔', '桃浦新村', '龙华',
                        '御桥', '龙耀路', '白银路', '嘉定新城', '安亭', '云锦路', '浦三路', '祁连山路', '昌吉东路', '枫桥路',
                        '马陆', '真如', '上海汽车城', '上海游泳馆', '花桥', '武威路', '光明路', '罗山路', '上海赛车场'];

         }
         else if(line=='12号线'){
             stations=['虹莘路', '宁国路', '提篮桥', '国际客运中心', '江浦公园', '七莘路', '隆昌路', '爱国路',
                        '桂林公园', '虹漕路', '顾戴路', '东陆路', '金京路', '申江路', '东兰路', '杨高北路', '虹梅路', '复兴岛'];
         }
         else if(line=='13号线'){
             stations=['金运路', '淮海中路', '世博会博物馆', '真北路', '大渡河路', '丰庄', '祁连山南路', '世博大道', '金沙江西路'];
         }
         else if(line=='16号线'){
             stations=['惠南', '鹤沙航城', '书院', '野生动物园', '周浦东', '滴水湖', '惠南东'];
         }
         else{
             stations=['汇金路', '漕盈路', '赵巷', '诸光路', '淀山湖大道', '青浦新城', '嘉松中路', '朱家角', '徐盈路', '蟠龙路', '徐泾北城'];
         }
         $('#nav2').empty();
         $.each(stations, function(i, item) {
                    $('#nav2').append("<li role=\"presentation\"><a href=\"?station="+item+"\">" + item + "</a></li>");
                });
         $('#navsubway li').removeClass('active');
         $(this).addClass('active');
    })
})
function getcommunitybybizcircle() {
    var input = $('#bizcircle').val();
    $.ajax({
        type: "post", //请求方式
        url: "../bizcircle_community/", //地址，就是json文件的请求路径
        data: {'input': input},
        //url: "http://localhost/community/bizcircle/" + input,
        //数据类型可以为 text xml json  script  jsonp
        success: function (result) {
            result = JSON.parse(result);
            //返回的参数就是 action里面所有的有get和set方法的参数
            if (result.length == 0) {
                $("#alert").html("<div class=\"alert alert-danger text-center\" role=\"alert\" id=\"alert\">不存在该商圈<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button></div>")
            } else {
                addGraph(result,input);
                addCommunityTable(result);
            }
        },
    })
}

    function getcommunitybystation() {
        var station = $('#station').val();
        $.ajax({
            type: "post", //请求方式
            url: "../station_community/", //地址，就是json文件的请求路径
            data: {'station': station},
            //url: "http://localhost/community/bizcircle/" + input,
            //数据类型可以为 text xml json  script  jsonp
            success: function (result) {
                result = JSON.parse(result);
                //返回的参数就是 action里面所有的有get和set方法的参数
                if (result.length == 0) {
                    $("#alert").html("<div class=\"alert alert-danger text-center\" role=\"alert\" id=\"alert\">不存在该地铁站<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button></div>")
                } else {
                    addGraph(result,station);
                    addCommunityTable(result);
                }
            },
        })
    }

        function addGraph(data,location) {
            var myChart = echarts.init(document.getElementById('chart-container'));
            var community_title = [];
            var volume = []
            for (var i = 0; i < data.length; i++) {
                if(data[i].onsale>0){
                community_title.push(data[i].title);
                volume.push(data[i].onsale);}
            }
            // 指定图表的配置项和数据
            var option = {
                title: {
                    text: '【'+location+'】周边小区房源',
                    textStyle: {
            color: '#ccc'
        }
                },
                backgroundColor: '#2c343c',
                tooltip: {show: true,},
                legend: {
                    data: ['在售房源'],
                    textStyle: {
            color: '#ccc'
        }
                },
                xAxis: {
                    data: community_title,
                    axisLabel: {
                        interval: 3,
                        rotate: 40,
                        textStyle: {
            color: '#ccc'
        }
                    }
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                yAxis: {axisLine:{
                    lineStyle:{
                        color: '#ccc',
                        width:1,
                    }
                    }},
                series: [{
                    name: '在售房源',
                    type: 'bar',
                    data: volume
                }]
            };
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
    }

    function addCommunityTable(result) {
        addHeader(result);
        var pages = (result.length / 20) + 1;
        if (result.length == 0) {
            $('<tr>').html("<td>搜索结果为空</td>").appendTo('#records_table');
        }

        if ($('#pagination-demo').data("twbs-pagination")) {
            $('#pagination-demo').twbsPagination('destroy');
        }

        $('#pagination-demo').twbsPagination({
            totalPages: pages,
            onPageClick: function (event, page) {
                var data = result.slice((page - 1) * 20, page * 20);
                addHeader(result);
                addData(data);
            }
        });

        function addHeader(result) {
            $("#records_table tr").remove();
            $('<tr>').html("<td>搜索结果:" + result.length + "个小区</td>").appendTo('#records_table');
            $('<tr class="info">').html("<td>名称</td><td>区县</td><td>参考均价</td><td>在售房源</td><td>建筑年代</td><td>建筑类型</td><td>物业费</td><td>物业公司</td><td>开发商</td><td>楼栋总数</td><td>房屋总数</td>").appendTo('#records_table');
        }

        function addData(result) {
            $.each(result, function (i, item) {
                $('<tr>').html(
                    "<td><a class='title'>" + result[i].title + "</a></td><td>" +
                    result[i].district + "</td><td>" +
                    result[i].price + "</td><td>" +
                    result[i].onsale + "</td><td>" +
                    result[i].year + "</td><td>" +
                    result[i].housetype + "</td><td>" +
                    result[i].cost + "</td><td>" +
                    result[i].service + "</td><td>" +
                    result[i].company + "</td><td>" +
                    result[i].building_num + "</td><td>" +
                    result[i].house_num + "</td>").appendTo('#records_table');
            });
        }
        $('.title').click(function () {
            var myForm = document.createElement("form");
myForm.method = "post";
myForm.action = "../community_detail/";
var myInput = document.createElement("input");
myInput.setAttribute("name", 'community'); // 为input对象设置name
myInput.setAttribute("value", $(this).text()); // 为input对象设置value
myForm.appendChild(myInput);
document.body.appendChild(myForm);
myForm.submit();
document.body.removeChild(myForm); // 提交后移除创建的form
        })
}