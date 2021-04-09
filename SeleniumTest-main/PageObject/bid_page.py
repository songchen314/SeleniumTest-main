from common.basepage import BasePage
import time
from PageLocators.invest_locators import Investlocators as Inv
class BidPage(BasePage):

        #投资
    def invest(self,invest_name):
        #在输入框中，输入金额
        #点击投资按钮
        time.sleep(2)
        doc="投资操作"
        self.input_text(Inv.invest_name,invest_name,doc)
        self.click_element(Inv.invest_button,doc)


    #获取用户余额
    def get_user_money(self):
        #

        pass

    #投资成功的提示框 - 点击激活
    def click_activeButton_on_success_popup(self):
        #

        pass

    #错误的提示框- - 非100的整数倍  页面中间
    def get_errorMsg(self):
        #获取文本内容
        #关闭弹窗

        pass
    #获取提示信息， --- 投标按钮上
    def get_errorMsg_from_investButton(self):

        pass



