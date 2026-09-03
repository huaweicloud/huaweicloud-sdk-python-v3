# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpeningInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'open': 'bool',
        'is_quota_exceed': 'bool',
        'quota_num': 'int',
        'used_num': 'int',
        'is_charge': 'bool'
    }

    attribute_map = {
        'open': 'open',
        'is_quota_exceed': 'is_quota_exceed',
        'quota_num': 'quota_num',
        'used_num': 'used_num',
        'is_charge': 'is_charge'
    }

    def __init__(self, open=None, is_quota_exceed=None, quota_num=None, used_num=None, is_charge=None):
        r"""ShowOpeningInfoResponse

        The model defined in huaweicloud sdk

        :param open: 是否开通
        :type open: bool
        :param is_quota_exceed: 配额是否超过
        :type is_quota_exceed: bool
        :param quota_num: 开通配额总数
        :type quota_num: int
        :param used_num: 已使用配额数量
        :type used_num: int
        :param is_charge: 是否付费
        :type is_charge: bool
        """
        
        super().__init__()

        self._open = None
        self._is_quota_exceed = None
        self._quota_num = None
        self._used_num = None
        self._is_charge = None
        self.discriminator = None

        if open is not None:
            self.open = open
        if is_quota_exceed is not None:
            self.is_quota_exceed = is_quota_exceed
        if quota_num is not None:
            self.quota_num = quota_num
        if used_num is not None:
            self.used_num = used_num
        if is_charge is not None:
            self.is_charge = is_charge

    @property
    def open(self):
        r"""Gets the open of this ShowOpeningInfoResponse.

        是否开通

        :return: The open of this ShowOpeningInfoResponse.
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        r"""Sets the open of this ShowOpeningInfoResponse.

        是否开通

        :param open: The open of this ShowOpeningInfoResponse.
        :type open: bool
        """
        self._open = open

    @property
    def is_quota_exceed(self):
        r"""Gets the is_quota_exceed of this ShowOpeningInfoResponse.

        配额是否超过

        :return: The is_quota_exceed of this ShowOpeningInfoResponse.
        :rtype: bool
        """
        return self._is_quota_exceed

    @is_quota_exceed.setter
    def is_quota_exceed(self, is_quota_exceed):
        r"""Sets the is_quota_exceed of this ShowOpeningInfoResponse.

        配额是否超过

        :param is_quota_exceed: The is_quota_exceed of this ShowOpeningInfoResponse.
        :type is_quota_exceed: bool
        """
        self._is_quota_exceed = is_quota_exceed

    @property
    def quota_num(self):
        r"""Gets the quota_num of this ShowOpeningInfoResponse.

        开通配额总数

        :return: The quota_num of this ShowOpeningInfoResponse.
        :rtype: int
        """
        return self._quota_num

    @quota_num.setter
    def quota_num(self, quota_num):
        r"""Sets the quota_num of this ShowOpeningInfoResponse.

        开通配额总数

        :param quota_num: The quota_num of this ShowOpeningInfoResponse.
        :type quota_num: int
        """
        self._quota_num = quota_num

    @property
    def used_num(self):
        r"""Gets the used_num of this ShowOpeningInfoResponse.

        已使用配额数量

        :return: The used_num of this ShowOpeningInfoResponse.
        :rtype: int
        """
        return self._used_num

    @used_num.setter
    def used_num(self, used_num):
        r"""Sets the used_num of this ShowOpeningInfoResponse.

        已使用配额数量

        :param used_num: The used_num of this ShowOpeningInfoResponse.
        :type used_num: int
        """
        self._used_num = used_num

    @property
    def is_charge(self):
        r"""Gets the is_charge of this ShowOpeningInfoResponse.

        是否付费

        :return: The is_charge of this ShowOpeningInfoResponse.
        :rtype: bool
        """
        return self._is_charge

    @is_charge.setter
    def is_charge(self, is_charge):
        r"""Sets the is_charge of this ShowOpeningInfoResponse.

        是否付费

        :param is_charge: The is_charge of this ShowOpeningInfoResponse.
        :type is_charge: bool
        """
        self._is_charge = is_charge

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpeningInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpeningInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
