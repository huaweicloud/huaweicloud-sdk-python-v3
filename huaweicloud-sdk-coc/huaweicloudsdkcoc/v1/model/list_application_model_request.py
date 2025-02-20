# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationModelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'component_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'page_no': 'int'
    }

    attribute_map = {
        'application_id': 'application_id',
        'component_id': 'component_id',
        'limit': 'limit',
        'marker': 'marker',
        'page_no': 'page_no'
    }

    def __init__(self, application_id=None, component_id=None, limit=None, marker=None, page_no=None):
        """ListApplicationModelRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用id
        :type application_id: str
        :param component_id: 组件id
        :type component_id: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，上一页请求最后一个id
        :type marker: str
        :param page_no: 分页页码
        :type page_no: int
        """
        
        

        self._application_id = None
        self._component_id = None
        self._limit = None
        self._marker = None
        self._page_no = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if component_id is not None:
            self.component_id = component_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_no is not None:
            self.page_no = page_no

    @property
    def application_id(self):
        """Gets the application_id of this ListApplicationModelRequest.

        应用id

        :return: The application_id of this ListApplicationModelRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ListApplicationModelRequest.

        应用id

        :param application_id: The application_id of this ListApplicationModelRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def component_id(self):
        """Gets the component_id of this ListApplicationModelRequest.

        组件id

        :return: The component_id of this ListApplicationModelRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ListApplicationModelRequest.

        组件id

        :param component_id: The component_id of this ListApplicationModelRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def limit(self):
        """Gets the limit of this ListApplicationModelRequest.

        最大的返回数量

        :return: The limit of this ListApplicationModelRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApplicationModelRequest.

        最大的返回数量

        :param limit: The limit of this ListApplicationModelRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListApplicationModelRequest.

        分页参数，上一页请求最后一个id

        :return: The marker of this ListApplicationModelRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListApplicationModelRequest.

        分页参数，上一页请求最后一个id

        :param marker: The marker of this ListApplicationModelRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_no(self):
        """Gets the page_no of this ListApplicationModelRequest.

        分页页码

        :return: The page_no of this ListApplicationModelRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ListApplicationModelRequest.

        分页页码

        :param page_no: The page_no of this ListApplicationModelRequest.
        :type page_no: int
        """
        self._page_no = page_no

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
        if not isinstance(other, ListApplicationModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
