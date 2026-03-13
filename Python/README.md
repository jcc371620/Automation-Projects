### Python脚本说明
-   Data_Cleaning.py: 数据清洗自动化
-   Auto Statistical Report: 自动生成统计报告
-   Batch File Processor: 批量处理多个文件
-   Auto Visualization: 自动可视化 + 保存图表
-   Scheduler (Run Daily): 定时自动运行（调度）

### pytest学习
1.  pytest test_cart.py --html=report.html --self-contained-html
    --html=report.html：创建一个叫 report.html 的网页文件。--self-contained-html：把图片和样式都塞进这一个文件里，方便你发邮件传给别人。
    
### pytest指令   
    pytest	//运行当前目录下所有符合规则的测试用例。

    pytest test_demo.py	//只运行某一个特定的测试文件。

    pytest -v	//--verbose
        详细模式，显示每个用例的执行结果（PASSED/FAILED）。
            区别： * 不加时： 每一个测试用例只显示一个点 . 或 F。如果跑 100 个用例，你只看到一堆点，不知道谁是谁。
            加了后： 它会列出每个测试文件的名字、每个测试函数的名称，并明确写出 PASSED（通过）或 FAILED（失败）。
            建议： 调试时必带，这样你能一眼看出哪个具体的函数挂了。

    pytest -s	//--capture=no
        显示print()打印信息，允许在控制台看到代码里的 print() 内容。默认情况下，pytest 会“吃掉”你代码里的 print() 内容，为了保持终端整洁。
            区别：不加时： 即使代码里写了 print("正在连接数据库")，你在终端也看不见。
            加了后： 它会关掉“捕捉”功能，把你代码里所有的 print 信息直接吐到终端。
            建议： 当你想通过打印信息来观察代码运行到哪一步时使用。

    pytest -k 	//--keyword
        用法： pytest -k "login"
        作用： 关键词匹配，它会搜寻并只运行所有名字里包含 "login" 的测试用例，其他的全部跳过。
        建议： 当你的测试文件里有 100 个用例，但你只想跑跟“登录”有关的那几个时，非常管用。

    pytest -x	//--exitfirst
        Exit on first failure (首错即停)
        遇到第一个错误就停止，不再继续往后跑。
        含义： “一旦出错，立即撤退”。
        作用： 正常情况下，pytest 即使遇到报错也会把剩下的跑完。加了 -x，只要有一个用例失败，它马上停止运行。
        建议： 当你在修复一个 Bug 时，不需要跑全量用例，只要看到它还没修好（报错了）就停下来继续改代码。当你只想修好某一个报错，不想看后面一大串报错的时候。

    pytest --maxfail=2	//允许报错的最大次数，达到次数后停止。

    pytest -vs //"V S 连跑"
        最推荐！ 既能看到详细名字，又能看到代码里的打印信息。
    
    pytest -v --html=res.html //"出报告"
        详细运行并把结果存成网页，发给开发看。


### pytest功能
1. 基础运行与发现（基础建设）
-   自动查找（Auto-discovery）： 
        只要文件名叫 test_*.py，函数名叫 test_*，它就能自动识别并运行，不需要手动登记。
-   断言重写（Assertion Rewriting）： 
    * 特点： 只需要写简单的 assert a == b。
        优势： 当测试失败时，pytest 会智能地展示出变量的具体值，而不是只告诉你“错了”。
-   标记机制（Marks）： 
    * 你可以给测试用例贴标签，比如 @pytest.mark.smoke（冒烟测试）。
        指令： pytest -m smoke 可以只运行带这个标签的用例。

2. 环境管理：Fixture（灵魂功能）
-   Fixture
-   依赖注入： 通过函数参数直接传递，不需要像传统方式那样写复杂的类继承。
-   灵活的作用域（Scope）： * function：每个函数跑一次（默认）。
        class：每个类跑一次
        module：每个文件跑一次
        session：最强招式，整个测试任务只跑一次（比如：整个项目测试开始前登录一次，结束后退出）。
-   yield 分层： 优雅地处理“前置准备”和“后置清理”。
-   conftest.py： 这是一个特殊文件，放在里面的 Fixture 可以被整个文件夹甚至子文件夹共享，实现“一次编写，全项目通用”。

3. 数据与逻辑控制（高效测试）
-   参数化（Parametrize）： * 作用： 逻辑不变，数据变
        优势： 实现“数据驱动测试”，极大减少代码冗余。
-   跳过与预期失败（Skip & Xfail）：
        @pytest.mark.skip：由于环境问题或功能没开发完，暂时跳过。
        @pytest.mark.xfail：已知有 Bug，预期它会失败（失败了不报错，成功了反而提醒你 Bug 可能修好了）。

4. 扩展性与报告（QA 的颜面）
-   强大的插件生态： pytest 本身很精简，但它有上千个插件。
        并行执行： pytest-xdist（让测试快如闪电）。
        失败重跑： pytest-rerunfailures（对付不稳定的网络请求）。
        顺序控制： pytest-ordering。
-   可视化报告：
        pytest-html： 生成静态 HTML 报告。
        Allure (常用)： 生成极其精美、带历史趋势图、带步骤截图的专业测试报告。
