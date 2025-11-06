# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDistributionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'distributor_instance_id': 'str',
        'distributor_instance_name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'distributor_instance_id': 'distributor_instance_id',
        'distributor_instance_name': 'distributor_instance_name'
    }

    def __init__(self, status=None, distributor_instance_id=None, distributor_instance_name=None):
        r"""ListDistributionResponse

        The model defined in huaweicloud sdk

        :param status: 状态。normal，abnormal，creating，createfail
        :type status: str
        :param distributor_instance_id: 分发服务器实例id。
        :type distributor_instance_id: str
        :param distributor_instance_name: 分发服务器实例名称。
        :type distributor_instance_name: str
        """
        
        super().__init__()

        self._status = None
        self._distributor_instance_id = None
        self._distributor_instance_name = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if distributor_instance_id is not None:
            self.distributor_instance_id = distributor_instance_id
        if distributor_instance_name is not None:
            self.distributor_instance_name = distributor_instance_name

    @property
    def status(self):
        r"""Gets the status of this ListDistributionResponse.

        状态。normal，abnormal，creating，createfail

        :return: The status of this ListDistributionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListDistributionResponse.

        状态。normal，abnormal，creating，createfail

        :param status: The status of this ListDistributionResponse.
        :type status: str
        """
        self._status = status

    @property
    def distributor_instance_id(self):
        r"""Gets the distributor_instance_id of this ListDistributionResponse.

        分发服务器实例id。

        :return: The distributor_instance_id of this ListDistributionResponse.
        :rtype: str
        """
        return self._distributor_instance_id

    @distributor_instance_id.setter
    def distributor_instance_id(self, distributor_instance_id):
        r"""Sets the distributor_instance_id of this ListDistributionResponse.

        分发服务器实例id。

        :param distributor_instance_id: The distributor_instance_id of this ListDistributionResponse.
        :type distributor_instance_id: str
        """
        self._distributor_instance_id = distributor_instance_id

    @property
    def distributor_instance_name(self):
        r"""Gets the distributor_instance_name of this ListDistributionResponse.

        分发服务器实例名称。

        :return: The distributor_instance_name of this ListDistributionResponse.
        :rtype: str
        """
        return self._distributor_instance_name

    @distributor_instance_name.setter
    def distributor_instance_name(self, distributor_instance_name):
        r"""Sets the distributor_instance_name of this ListDistributionResponse.

        分发服务器实例名称。

        :param distributor_instance_name: The distributor_instance_name of this ListDistributionResponse.
        :type distributor_instance_name: str
        """
        self._distributor_instance_name = distributor_instance_name

    def to_dict(self):
        import warnings
        warnings.warn("ListDistributionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDistributionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
