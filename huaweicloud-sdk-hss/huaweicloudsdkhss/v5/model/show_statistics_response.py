# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vault_host_num': 'int',
        'rasp_host_num': 'int',
        'wtp_host_num': 'int',
        'two_factor_host_num': 'int',
        'isolated_file_num': 'int',
        'support_two_factor_host_num': 'int',
        'app_process_host_num': 'int'
    }

    attribute_map = {
        'vault_host_num': 'vault_host_num',
        'rasp_host_num': 'rasp_host_num',
        'wtp_host_num': 'wtp_host_num',
        'two_factor_host_num': 'two_factor_host_num',
        'isolated_file_num': 'isolated_file_num',
        'support_two_factor_host_num': 'support_two_factor_host_num',
        'app_process_host_num': 'app_process_host_num'
    }

    def __init__(self, vault_host_num=None, rasp_host_num=None, wtp_host_num=None, two_factor_host_num=None, isolated_file_num=None, support_two_factor_host_num=None, app_process_host_num=None):
        r"""ShowStatisticsResponse

        The model defined in huaweicloud sdk

        :param vault_host_num: **参数解释**: 勒索病毒防护开启主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type vault_host_num: int
        :param rasp_host_num: **参数解释**: 应用防护开启主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type rasp_host_num: int
        :param wtp_host_num: **参数解释**: 网页防篡改开启主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type wtp_host_num: int
        :param two_factor_host_num: **参数解释**: 双因子认证开启主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type two_factor_host_num: int
        :param isolated_file_num: **参数解释**: 隔离文件数量 **取值范围**: 最小值0，最大值2147483647 
        :type isolated_file_num: int
        :param support_two_factor_host_num: **参数解释**: 支持开启双因子的主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type support_two_factor_host_num: int
        :param app_process_host_num: **参数解释**: 开启应用进程的主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type app_process_host_num: int
        """
        
        super().__init__()

        self._vault_host_num = None
        self._rasp_host_num = None
        self._wtp_host_num = None
        self._two_factor_host_num = None
        self._isolated_file_num = None
        self._support_two_factor_host_num = None
        self._app_process_host_num = None
        self.discriminator = None

        if vault_host_num is not None:
            self.vault_host_num = vault_host_num
        if rasp_host_num is not None:
            self.rasp_host_num = rasp_host_num
        if wtp_host_num is not None:
            self.wtp_host_num = wtp_host_num
        if two_factor_host_num is not None:
            self.two_factor_host_num = two_factor_host_num
        if isolated_file_num is not None:
            self.isolated_file_num = isolated_file_num
        if support_two_factor_host_num is not None:
            self.support_two_factor_host_num = support_two_factor_host_num
        if app_process_host_num is not None:
            self.app_process_host_num = app_process_host_num

    @property
    def vault_host_num(self):
        r"""Gets the vault_host_num of this ShowStatisticsResponse.

        **参数解释**: 勒索病毒防护开启主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The vault_host_num of this ShowStatisticsResponse.
        :rtype: int
        """
        return self._vault_host_num

    @vault_host_num.setter
    def vault_host_num(self, vault_host_num):
        r"""Sets the vault_host_num of this ShowStatisticsResponse.

        **参数解释**: 勒索病毒防护开启主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param vault_host_num: The vault_host_num of this ShowStatisticsResponse.
        :type vault_host_num: int
        """
        self._vault_host_num = vault_host_num

    @property
    def rasp_host_num(self):
        r"""Gets the rasp_host_num of this ShowStatisticsResponse.

        **参数解释**: 应用防护开启主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The rasp_host_num of this ShowStatisticsResponse.
        :rtype: int
        """
        return self._rasp_host_num

    @rasp_host_num.setter
    def rasp_host_num(self, rasp_host_num):
        r"""Sets the rasp_host_num of this ShowStatisticsResponse.

        **参数解释**: 应用防护开启主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param rasp_host_num: The rasp_host_num of this ShowStatisticsResponse.
        :type rasp_host_num: int
        """
        self._rasp_host_num = rasp_host_num

    @property
    def wtp_host_num(self):
        r"""Gets the wtp_host_num of this ShowStatisticsResponse.

        **参数解释**: 网页防篡改开启主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The wtp_host_num of this ShowStatisticsResponse.
        :rtype: int
        """
        return self._wtp_host_num

    @wtp_host_num.setter
    def wtp_host_num(self, wtp_host_num):
        r"""Sets the wtp_host_num of this ShowStatisticsResponse.

        **参数解释**: 网页防篡改开启主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param wtp_host_num: The wtp_host_num of this ShowStatisticsResponse.
        :type wtp_host_num: int
        """
        self._wtp_host_num = wtp_host_num

    @property
    def two_factor_host_num(self):
        r"""Gets the two_factor_host_num of this ShowStatisticsResponse.

        **参数解释**: 双因子认证开启主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The two_factor_host_num of this ShowStatisticsResponse.
        :rtype: int
        """
        return self._two_factor_host_num

    @two_factor_host_num.setter
    def two_factor_host_num(self, two_factor_host_num):
        r"""Sets the two_factor_host_num of this ShowStatisticsResponse.

        **参数解释**: 双因子认证开启主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param two_factor_host_num: The two_factor_host_num of this ShowStatisticsResponse.
        :type two_factor_host_num: int
        """
        self._two_factor_host_num = two_factor_host_num

    @property
    def isolated_file_num(self):
        r"""Gets the isolated_file_num of this ShowStatisticsResponse.

        **参数解释**: 隔离文件数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The isolated_file_num of this ShowStatisticsResponse.
        :rtype: int
        """
        return self._isolated_file_num

    @isolated_file_num.setter
    def isolated_file_num(self, isolated_file_num):
        r"""Sets the isolated_file_num of this ShowStatisticsResponse.

        **参数解释**: 隔离文件数量 **取值范围**: 最小值0，最大值2147483647 

        :param isolated_file_num: The isolated_file_num of this ShowStatisticsResponse.
        :type isolated_file_num: int
        """
        self._isolated_file_num = isolated_file_num

    @property
    def support_two_factor_host_num(self):
        r"""Gets the support_two_factor_host_num of this ShowStatisticsResponse.

        **参数解释**: 支持开启双因子的主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The support_two_factor_host_num of this ShowStatisticsResponse.
        :rtype: int
        """
        return self._support_two_factor_host_num

    @support_two_factor_host_num.setter
    def support_two_factor_host_num(self, support_two_factor_host_num):
        r"""Sets the support_two_factor_host_num of this ShowStatisticsResponse.

        **参数解释**: 支持开启双因子的主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param support_two_factor_host_num: The support_two_factor_host_num of this ShowStatisticsResponse.
        :type support_two_factor_host_num: int
        """
        self._support_two_factor_host_num = support_two_factor_host_num

    @property
    def app_process_host_num(self):
        r"""Gets the app_process_host_num of this ShowStatisticsResponse.

        **参数解释**: 开启应用进程的主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The app_process_host_num of this ShowStatisticsResponse.
        :rtype: int
        """
        return self._app_process_host_num

    @app_process_host_num.setter
    def app_process_host_num(self, app_process_host_num):
        r"""Sets the app_process_host_num of this ShowStatisticsResponse.

        **参数解释**: 开启应用进程的主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param app_process_host_num: The app_process_host_num of this ShowStatisticsResponse.
        :type app_process_host_num: int
        """
        self._app_process_host_num = app_process_host_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatisticsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
