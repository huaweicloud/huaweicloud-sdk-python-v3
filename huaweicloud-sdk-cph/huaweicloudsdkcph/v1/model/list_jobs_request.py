# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'request_ids': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'request_id': 'request_id',
        'request_ids': 'request_ids',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, request_id=None, request_ids=None, offset=None, limit=None):
        r"""ListJobsRequest

        The model defined in huaweicloud sdk

        :param request_id: 任务下发请求时响应的request_id。 request_id和request_ids必须指定其中一个。request_id和request_ids同时指定的时候，以request_ids为准。
        :type request_id: str
        :param request_ids: 任务下发请求时响应的多个request_id，用逗号分隔，最多不能超过20个。 request_id和request_ids必须指定其中一个。request_id和request_ids同时指定的时候，以request_ids为准。
        :type request_ids: str
        :param offset: 偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。
        :type offset: int
        :param limit: 每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        """
        
        

        self._request_id = None
        self._request_ids = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if request_ids is not None:
            self.request_ids = request_ids
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def request_id(self):
        r"""Gets the request_id of this ListJobsRequest.

        任务下发请求时响应的request_id。 request_id和request_ids必须指定其中一个。request_id和request_ids同时指定的时候，以request_ids为准。

        :return: The request_id of this ListJobsRequest.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListJobsRequest.

        任务下发请求时响应的request_id。 request_id和request_ids必须指定其中一个。request_id和request_ids同时指定的时候，以request_ids为准。

        :param request_id: The request_id of this ListJobsRequest.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def request_ids(self):
        r"""Gets the request_ids of this ListJobsRequest.

        任务下发请求时响应的多个request_id，用逗号分隔，最多不能超过20个。 request_id和request_ids必须指定其中一个。request_id和request_ids同时指定的时候，以request_ids为准。

        :return: The request_ids of this ListJobsRequest.
        :rtype: str
        """
        return self._request_ids

    @request_ids.setter
    def request_ids(self, request_ids):
        r"""Sets the request_ids of this ListJobsRequest.

        任务下发请求时响应的多个request_id，用逗号分隔，最多不能超过20个。 request_id和request_ids必须指定其中一个。request_id和request_ids同时指定的时候，以request_ids为准。

        :param request_ids: The request_ids of this ListJobsRequest.
        :type request_ids: str
        """
        self._request_ids = request_ids

    @property
    def offset(self):
        r"""Gets the offset of this ListJobsRequest.

        偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :return: The offset of this ListJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobsRequest.

        偏移量为一个大于等于0整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :param offset: The offset of this ListJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListJobsRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobsRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListJobsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
