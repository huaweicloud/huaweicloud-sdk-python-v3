# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance': 'InstancesVO',
        'status': 'str',
        'bundle_url': 'str'
    }

    attribute_map = {
        'instance': 'instance',
        'status': 'status',
        'bundle_url': 'bundle_url'
    }

    def __init__(self, instance=None, status=None, bundle_url=None):
        """ShowInstanceResponse

        The model defined in huaweicloud sdk

        :param instance: 
        :type instance: :class:`huaweicloudsdkcloudide.v2.InstancesVO`
        :param status: 状态
        :type status: str
        :param bundle_url: 静态资源链接
        :type bundle_url: str
        """
        
        super(ShowInstanceResponse, self).__init__()

        self._instance = None
        self._status = None
        self._bundle_url = None
        self.discriminator = None

        if instance is not None:
            self.instance = instance
        if status is not None:
            self.status = status
        if bundle_url is not None:
            self.bundle_url = bundle_url

    @property
    def instance(self):
        """Gets the instance of this ShowInstanceResponse.


        :return: The instance of this ShowInstanceResponse.
        :rtype: :class:`huaweicloudsdkcloudide.v2.InstancesVO`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ShowInstanceResponse.


        :param instance: The instance of this ShowInstanceResponse.
        :type instance: :class:`huaweicloudsdkcloudide.v2.InstancesVO`
        """
        self._instance = instance

    @property
    def status(self):
        """Gets the status of this ShowInstanceResponse.

        状态

        :return: The status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowInstanceResponse.

        状态

        :param status: The status of this ShowInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def bundle_url(self):
        """Gets the bundle_url of this ShowInstanceResponse.

        静态资源链接

        :return: The bundle_url of this ShowInstanceResponse.
        :rtype: str
        """
        return self._bundle_url

    @bundle_url.setter
    def bundle_url(self, bundle_url):
        """Sets the bundle_url of this ShowInstanceResponse.

        静态资源链接

        :param bundle_url: The bundle_url of this ShowInstanceResponse.
        :type bundle_url: str
        """
        self._bundle_url = bundle_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
