# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'list[str]',
        'business_id': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'business_id': 'business_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, resource=None, business_id=None, begin_time=None, end_time=None):
        r"""SearchTaskRequest

        The model defined in huaweicloud sdk

        :param resource: 资源类型
        :type resource: list[str]
        :param business_id: 业务id,比如问答时传入skill_id
        :type business_id: str
        :param begin_time: 开始时间戳
        :type begin_time: str
        :param end_time: 结束时间戳
        :type end_time: str
        """
        
        

        self._resource = None
        self._business_id = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if business_id is not None:
            self.business_id = business_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def resource(self):
        r"""Gets the resource of this SearchTaskRequest.

        资源类型

        :return: The resource of this SearchTaskRequest.
        :rtype: list[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this SearchTaskRequest.

        资源类型

        :param resource: The resource of this SearchTaskRequest.
        :type resource: list[str]
        """
        self._resource = resource

    @property
    def business_id(self):
        r"""Gets the business_id of this SearchTaskRequest.

        业务id,比如问答时传入skill_id

        :return: The business_id of this SearchTaskRequest.
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this SearchTaskRequest.

        业务id,比如问答时传入skill_id

        :param business_id: The business_id of this SearchTaskRequest.
        :type business_id: str
        """
        self._business_id = business_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this SearchTaskRequest.

        开始时间戳

        :return: The begin_time of this SearchTaskRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this SearchTaskRequest.

        开始时间戳

        :param begin_time: The begin_time of this SearchTaskRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SearchTaskRequest.

        结束时间戳

        :return: The end_time of this SearchTaskRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SearchTaskRequest.

        结束时间戳

        :param end_time: The end_time of this SearchTaskRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, SearchTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
