# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_instances': 'list[QueryAppInstanceResp]'
    }

    attribute_map = {
        'app_instances': 'app_instances'
    }

    def __init__(self, app_instances=None):
        r"""ListAppInstancesResponse

        The model defined in huaweicloud sdk

        :param app_instances: 应用实例列表
        :type app_instances: list[:class:`huaweicloudsdkiotedge.v3.QueryAppInstanceResp`]
        """
        
        super(ListAppInstancesResponse, self).__init__()

        self._app_instances = None
        self.discriminator = None

        if app_instances is not None:
            self.app_instances = app_instances

    @property
    def app_instances(self):
        r"""Gets the app_instances of this ListAppInstancesResponse.

        应用实例列表

        :return: The app_instances of this ListAppInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.QueryAppInstanceResp`]
        """
        return self._app_instances

    @app_instances.setter
    def app_instances(self, app_instances):
        r"""Sets the app_instances of this ListAppInstancesResponse.

        应用实例列表

        :param app_instances: The app_instances of this ListAppInstancesResponse.
        :type app_instances: list[:class:`huaweicloudsdkiotedge.v3.QueryAppInstanceResp`]
        """
        self._app_instances = app_instances

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
        if not isinstance(other, ListAppInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
