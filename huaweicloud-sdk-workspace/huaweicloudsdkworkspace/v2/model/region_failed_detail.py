# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegionFailedDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'region': 'region',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, region=None, error_code=None, error_msg=None):
        r"""RegionFailedDetail

        The model defined in huaweicloud sdk

        :param region: 失败的区域标识。
        :type region: str
        :param error_code: 错误码，格式 WKS.XXXXXXXX。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        

        self._region = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def region(self):
        r"""Gets the region of this RegionFailedDetail.

        失败的区域标识。

        :return: The region of this RegionFailedDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RegionFailedDetail.

        失败的区域标识。

        :param region: The region of this RegionFailedDetail.
        :type region: str
        """
        self._region = region

    @property
    def error_code(self):
        r"""Gets the error_code of this RegionFailedDetail.

        错误码，格式 WKS.XXXXXXXX。

        :return: The error_code of this RegionFailedDetail.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this RegionFailedDetail.

        错误码，格式 WKS.XXXXXXXX。

        :param error_code: The error_code of this RegionFailedDetail.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this RegionFailedDetail.

        错误信息。

        :return: The error_msg of this RegionFailedDetail.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this RegionFailedDetail.

        错误信息。

        :param error_msg: The error_msg of this RegionFailedDetail.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, RegionFailedDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
