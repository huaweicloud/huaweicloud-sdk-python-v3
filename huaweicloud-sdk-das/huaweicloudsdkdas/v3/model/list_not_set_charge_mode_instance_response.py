# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotSetChargeModeInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_list': 'list[InstanceSimpleDto]',
        'quota_status': 'int',
        'quota_num': 'int',
        'used_num': 'int'
    }

    attribute_map = {
        'instance_list': 'instance_list',
        'quota_status': 'quota_status',
        'quota_num': 'quota_num',
        'used_num': 'used_num'
    }

    def __init__(self, instance_list=None, quota_status=None, quota_num=None, used_num=None):
        r"""ListNotSetChargeModeInstanceResponse

        The model defined in huaweicloud sdk

        :param instance_list: 实例列表
        :type instance_list: list[:class:`huaweicloudsdkdas.v3.InstanceSimpleDto`]
        :param quota_status: 付费状态。取值范围：0（免费实例）、1（付费实例）
        :type quota_status: int
        :param quota_num: 开通配额总数
        :type quota_num: int
        :param used_num: 已使用配额数量
        :type used_num: int
        """
        
        super().__init__()

        self._instance_list = None
        self._quota_status = None
        self._quota_num = None
        self._used_num = None
        self.discriminator = None

        if instance_list is not None:
            self.instance_list = instance_list
        if quota_status is not None:
            self.quota_status = quota_status
        if quota_num is not None:
            self.quota_num = quota_num
        if used_num is not None:
            self.used_num = used_num

    @property
    def instance_list(self):
        r"""Gets the instance_list of this ListNotSetChargeModeInstanceResponse.

        实例列表

        :return: The instance_list of this ListNotSetChargeModeInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InstanceSimpleDto`]
        """
        return self._instance_list

    @instance_list.setter
    def instance_list(self, instance_list):
        r"""Sets the instance_list of this ListNotSetChargeModeInstanceResponse.

        实例列表

        :param instance_list: The instance_list of this ListNotSetChargeModeInstanceResponse.
        :type instance_list: list[:class:`huaweicloudsdkdas.v3.InstanceSimpleDto`]
        """
        self._instance_list = instance_list

    @property
    def quota_status(self):
        r"""Gets the quota_status of this ListNotSetChargeModeInstanceResponse.

        付费状态。取值范围：0（免费实例）、1（付费实例）

        :return: The quota_status of this ListNotSetChargeModeInstanceResponse.
        :rtype: int
        """
        return self._quota_status

    @quota_status.setter
    def quota_status(self, quota_status):
        r"""Sets the quota_status of this ListNotSetChargeModeInstanceResponse.

        付费状态。取值范围：0（免费实例）、1（付费实例）

        :param quota_status: The quota_status of this ListNotSetChargeModeInstanceResponse.
        :type quota_status: int
        """
        self._quota_status = quota_status

    @property
    def quota_num(self):
        r"""Gets the quota_num of this ListNotSetChargeModeInstanceResponse.

        开通配额总数

        :return: The quota_num of this ListNotSetChargeModeInstanceResponse.
        :rtype: int
        """
        return self._quota_num

    @quota_num.setter
    def quota_num(self, quota_num):
        r"""Sets the quota_num of this ListNotSetChargeModeInstanceResponse.

        开通配额总数

        :param quota_num: The quota_num of this ListNotSetChargeModeInstanceResponse.
        :type quota_num: int
        """
        self._quota_num = quota_num

    @property
    def used_num(self):
        r"""Gets the used_num of this ListNotSetChargeModeInstanceResponse.

        已使用配额数量

        :return: The used_num of this ListNotSetChargeModeInstanceResponse.
        :rtype: int
        """
        return self._used_num

    @used_num.setter
    def used_num(self, used_num):
        r"""Sets the used_num of this ListNotSetChargeModeInstanceResponse.

        已使用配额数量

        :param used_num: The used_num of this ListNotSetChargeModeInstanceResponse.
        :type used_num: int
        """
        self._used_num = used_num

    def to_dict(self):
        import warnings
        warnings.warn("ListNotSetChargeModeInstanceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListNotSetChargeModeInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
