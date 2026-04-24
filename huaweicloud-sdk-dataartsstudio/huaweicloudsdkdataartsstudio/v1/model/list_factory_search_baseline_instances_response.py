# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactorySearchBaselineInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'baseline_instances': 'list[BaselineInstance]'
    }

    attribute_map = {
        'total': 'total',
        'baseline_instances': 'baseline_instances'
    }

    def __init__(self, total=None, baseline_instances=None):
        r"""ListFactorySearchBaselineInstancesResponse

        The model defined in huaweicloud sdk

        :param total: 基线实例总数。
        :type total: int
        :param baseline_instances: 基线实例列表信息。
        :type baseline_instances: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineInstance`]
        """
        
        super().__init__()

        self._total = None
        self._baseline_instances = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if baseline_instances is not None:
            self.baseline_instances = baseline_instances

    @property
    def total(self):
        r"""Gets the total of this ListFactorySearchBaselineInstancesResponse.

        基线实例总数。

        :return: The total of this ListFactorySearchBaselineInstancesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFactorySearchBaselineInstancesResponse.

        基线实例总数。

        :param total: The total of this ListFactorySearchBaselineInstancesResponse.
        :type total: int
        """
        self._total = total

    @property
    def baseline_instances(self):
        r"""Gets the baseline_instances of this ListFactorySearchBaselineInstancesResponse.

        基线实例列表信息。

        :return: The baseline_instances of this ListFactorySearchBaselineInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineInstance`]
        """
        return self._baseline_instances

    @baseline_instances.setter
    def baseline_instances(self, baseline_instances):
        r"""Sets the baseline_instances of this ListFactorySearchBaselineInstancesResponse.

        基线实例列表信息。

        :param baseline_instances: The baseline_instances of this ListFactorySearchBaselineInstancesResponse.
        :type baseline_instances: list[:class:`huaweicloudsdkdataartsstudio.v1.BaselineInstance`]
        """
        self._baseline_instances = baseline_instances

    def to_dict(self):
        import warnings
        warnings.warn("ListFactorySearchBaselineInstancesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListFactorySearchBaselineInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
