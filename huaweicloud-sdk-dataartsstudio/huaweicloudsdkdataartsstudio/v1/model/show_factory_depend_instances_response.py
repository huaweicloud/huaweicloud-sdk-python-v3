# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryDependInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'depend_instances_info': 'list[ShowFactoryDependInstancesRespDependInstancesInfo]',
        'total': 'int'
    }

    attribute_map = {
        'depend_instances_info': 'depend_instances_info',
        'total': 'total'
    }

    def __init__(self, depend_instances_info=None, total=None):
        r"""ShowFactoryDependInstancesResponse

        The model defined in huaweicloud sdk

        :param depend_instances_info: 实例详情。
        :type depend_instances_info: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowFactoryDependInstancesRespDependInstancesInfo`]
        :param total: 返回的实例总数。
        :type total: int
        """
        
        super().__init__()

        self._depend_instances_info = None
        self._total = None
        self.discriminator = None

        if depend_instances_info is not None:
            self.depend_instances_info = depend_instances_info
        if total is not None:
            self.total = total

    @property
    def depend_instances_info(self):
        r"""Gets the depend_instances_info of this ShowFactoryDependInstancesResponse.

        实例详情。

        :return: The depend_instances_info of this ShowFactoryDependInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowFactoryDependInstancesRespDependInstancesInfo`]
        """
        return self._depend_instances_info

    @depend_instances_info.setter
    def depend_instances_info(self, depend_instances_info):
        r"""Sets the depend_instances_info of this ShowFactoryDependInstancesResponse.

        实例详情。

        :param depend_instances_info: The depend_instances_info of this ShowFactoryDependInstancesResponse.
        :type depend_instances_info: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowFactoryDependInstancesRespDependInstancesInfo`]
        """
        self._depend_instances_info = depend_instances_info

    @property
    def total(self):
        r"""Gets the total of this ShowFactoryDependInstancesResponse.

        返回的实例总数。

        :return: The total of this ShowFactoryDependInstancesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowFactoryDependInstancesResponse.

        返回的实例总数。

        :param total: The total of this ShowFactoryDependInstancesResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ShowFactoryDependInstancesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowFactoryDependInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
