# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSupportKeyStringResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'support_key_str': 'bool',
        'instance_type': 'str',
        'instance_detail_version': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'support_key_str': 'support_key_str',
        'instance_type': 'instance_type',
        'instance_detail_version': 'instance_detail_version',
        'error_msg': 'error_msg'
    }

    def __init__(self, support_key_str=None, instance_type=None, instance_detail_version=None, error_msg=None):
        r"""ShowSupportKeyStringResponse

        The model defined in huaweicloud sdk

        :param support_key_str: 实例是否使用关键字自治限流功能。true：可用，false：不可用
        :type support_key_str: bool
        :param instance_type: 实例类型
        :type instance_type: str
        :param instance_detail_version: 实例详细版本号
        :type instance_detail_version: str
        :param error_msg: 当support_key_str为False时展示errorMsg
        :type error_msg: str
        """
        
        super().__init__()

        self._support_key_str = None
        self._instance_type = None
        self._instance_detail_version = None
        self._error_msg = None
        self.discriminator = None

        if support_key_str is not None:
            self.support_key_str = support_key_str
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_detail_version is not None:
            self.instance_detail_version = instance_detail_version
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def support_key_str(self):
        r"""Gets the support_key_str of this ShowSupportKeyStringResponse.

        实例是否使用关键字自治限流功能。true：可用，false：不可用

        :return: The support_key_str of this ShowSupportKeyStringResponse.
        :rtype: bool
        """
        return self._support_key_str

    @support_key_str.setter
    def support_key_str(self, support_key_str):
        r"""Sets the support_key_str of this ShowSupportKeyStringResponse.

        实例是否使用关键字自治限流功能。true：可用，false：不可用

        :param support_key_str: The support_key_str of this ShowSupportKeyStringResponse.
        :type support_key_str: bool
        """
        self._support_key_str = support_key_str

    @property
    def instance_type(self):
        r"""Gets the instance_type of this ShowSupportKeyStringResponse.

        实例类型

        :return: The instance_type of this ShowSupportKeyStringResponse.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this ShowSupportKeyStringResponse.

        实例类型

        :param instance_type: The instance_type of this ShowSupportKeyStringResponse.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_detail_version(self):
        r"""Gets the instance_detail_version of this ShowSupportKeyStringResponse.

        实例详细版本号

        :return: The instance_detail_version of this ShowSupportKeyStringResponse.
        :rtype: str
        """
        return self._instance_detail_version

    @instance_detail_version.setter
    def instance_detail_version(self, instance_detail_version):
        r"""Sets the instance_detail_version of this ShowSupportKeyStringResponse.

        实例详细版本号

        :param instance_detail_version: The instance_detail_version of this ShowSupportKeyStringResponse.
        :type instance_detail_version: str
        """
        self._instance_detail_version = instance_detail_version

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowSupportKeyStringResponse.

        当support_key_str为False时展示errorMsg

        :return: The error_msg of this ShowSupportKeyStringResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowSupportKeyStringResponse.

        当support_key_str为False时展示errorMsg

        :param error_msg: The error_msg of this ShowSupportKeyStringResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    def to_dict(self):
        import warnings
        warnings.warn("ShowSupportKeyStringResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSupportKeyStringResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
