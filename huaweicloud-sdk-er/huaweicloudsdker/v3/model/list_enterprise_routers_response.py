# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseRoutersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances': 'list[EnterpriseRouter]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'instances': 'instances',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, instances=None, page_info=None, request_id=None):
        """ListEnterpriseRoutersResponse

        The model defined in huaweicloud sdk

        :param instances: 企业路由器列表
        :type instances: list[:class:`huaweicloudsdker.v3.EnterpriseRouter`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ListEnterpriseRoutersResponse, self).__init__()

        self._instances = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def instances(self):
        """Gets the instances of this ListEnterpriseRoutersResponse.

        企业路由器列表

        :return: The instances of this ListEnterpriseRoutersResponse.
        :rtype: list[:class:`huaweicloudsdker.v3.EnterpriseRouter`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListEnterpriseRoutersResponse.

        企业路由器列表

        :param instances: The instances of this ListEnterpriseRoutersResponse.
        :type instances: list[:class:`huaweicloudsdker.v3.EnterpriseRouter`]
        """
        self._instances = instances

    @property
    def page_info(self):
        """Gets the page_info of this ListEnterpriseRoutersResponse.

        :return: The page_info of this ListEnterpriseRoutersResponse.
        :rtype: :class:`huaweicloudsdker.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListEnterpriseRoutersResponse.

        :param page_info: The page_info of this ListEnterpriseRoutersResponse.
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListEnterpriseRoutersResponse.

        请求ID

        :return: The request_id of this ListEnterpriseRoutersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListEnterpriseRoutersResponse.

        请求ID

        :param request_id: The request_id of this ListEnterpriseRoutersResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListEnterpriseRoutersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
