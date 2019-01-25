import allure

class Test_001:
    @allure.step(title="我是测试步骤1")
    def test_001(self):
        print('0001')
        assert True

    @allure.step(title="我是测试步骤22222")
    def test_002(self):
        print('002')
        assert False