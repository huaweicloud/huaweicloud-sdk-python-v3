# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'setting_name': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'setting_name': 'setting_name',
        'region_id': 'region_id'
    }

    def __init__(self, error_code=None, error_msg=None, setting_name=None, region_id=None):
        r"""ErrorInfo

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误消息
        :type error_msg: str
        :param setting_name: 规则的配置名称
        :type setting_name: str
        :param region_id: region的ID
        :type region_id: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._setting_name = None
        self._region_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if setting_name is not None:
            self.setting_name = setting_name
        if region_id is not None:
            self.region_id = region_id

    @property
    def error_code(self):
        r"""Gets the error_code of this ErrorInfo.

        错误码

        :return: The error_code of this ErrorInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ErrorInfo.

        错误码

        :param error_code: The error_code of this ErrorInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ErrorInfo.

        错误消息

        :return: The error_msg of this ErrorInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ErrorInfo.

        错误消息

        :param error_msg: The error_msg of this ErrorInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def setting_name(self):
        r"""Gets the setting_name of this ErrorInfo.

        规则的配置名称

        :return: The setting_name of this ErrorInfo.
        :rtype: str
        """
        return self._setting_name

    @setting_name.setter
    def setting_name(self, setting_name):
        r"""Sets the setting_name of this ErrorInfo.

        规则的配置名称

        :param setting_name: The setting_name of this ErrorInfo.
        :type setting_name: str
        """
        self._setting_name = setting_name

    @property
    def region_id(self):
        r"""Gets the region_id of this ErrorInfo.

        region的ID

        :return: The region_id of this ErrorInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ErrorInfo.

        region的ID

        :param region_id: The region_id of this ErrorInfo.
        :type region_id: str
        """
        self._region_id = region_id

    def to_dict(self):
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
        if not isinstance(other, ErrorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
