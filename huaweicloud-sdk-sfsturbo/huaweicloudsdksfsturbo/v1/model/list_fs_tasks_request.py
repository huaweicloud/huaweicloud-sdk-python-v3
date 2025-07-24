# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFsTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'feature': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'share_id': 'share_id',
        'feature': 'feature',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, share_id=None, feature=None, marker=None, limit=None):
        r"""ListFsTasksRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统id
        :type share_id: str
        :param feature: 任务类型。例，DU任务取值为dir-usage
        :type feature: str
        :param marker: marker填写为上一页返回的最后一条记录的task_id，作为下一次分页的起始值。比如，marker为d651ea2b-2b20-4c6d-8bbf-2adcec18dac9，limit为100，表示从d651ea2b-2b20-4c6d-8bbf-2adcec18dac9后返回最多100条满足查询条件的记录。
        :type marker: str
        :param limit: limit, 取值为正整数. 默认为20，最大值为100
        :type limit: int
        """
        
        

        self._share_id = None
        self._feature = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.share_id = share_id
        self.feature = feature
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def share_id(self):
        r"""Gets the share_id of this ListFsTasksRequest.

        文件系统id

        :return: The share_id of this ListFsTasksRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        r"""Sets the share_id of this ListFsTasksRequest.

        文件系统id

        :param share_id: The share_id of this ListFsTasksRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def feature(self):
        r"""Gets the feature of this ListFsTasksRequest.

        任务类型。例，DU任务取值为dir-usage

        :return: The feature of this ListFsTasksRequest.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this ListFsTasksRequest.

        任务类型。例，DU任务取值为dir-usage

        :param feature: The feature of this ListFsTasksRequest.
        :type feature: str
        """
        self._feature = feature

    @property
    def marker(self):
        r"""Gets the marker of this ListFsTasksRequest.

        marker填写为上一页返回的最后一条记录的task_id，作为下一次分页的起始值。比如，marker为d651ea2b-2b20-4c6d-8bbf-2adcec18dac9，limit为100，表示从d651ea2b-2b20-4c6d-8bbf-2adcec18dac9后返回最多100条满足查询条件的记录。

        :return: The marker of this ListFsTasksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFsTasksRequest.

        marker填写为上一页返回的最后一条记录的task_id，作为下一次分页的起始值。比如，marker为d651ea2b-2b20-4c6d-8bbf-2adcec18dac9，limit为100，表示从d651ea2b-2b20-4c6d-8bbf-2adcec18dac9后返回最多100条满足查询条件的记录。

        :param marker: The marker of this ListFsTasksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListFsTasksRequest.

        limit, 取值为正整数. 默认为20，最大值为100

        :return: The limit of this ListFsTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFsTasksRequest.

        limit, 取值为正整数. 默认为20，最大值为100

        :param limit: The limit of this ListFsTasksRequest.
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
        if not isinstance(other, ListFsTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
