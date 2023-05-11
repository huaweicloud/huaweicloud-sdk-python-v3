# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchCriteriasBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'criterias': 'list[GetQuerySearchCriteriasBody]',
        'log_stream_id': 'str',
        'log_stream_name': 'str'
    }

    attribute_map = {
        'criterias': 'criterias',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name'
    }

    def __init__(self, criterias=None, log_stream_id=None, log_stream_name=None):
        """SearchCriteriasBody

        The model defined in huaweicloud sdk

        :param criterias: 单个日志流的快速查询
        :type criterias: list[:class:`huaweicloudsdklts.v2.GetQuerySearchCriteriasBody`]
        :param log_stream_id: 日志流id
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        """
        
        

        self._criterias = None
        self._log_stream_id = None
        self._log_stream_name = None
        self.discriminator = None

        self.criterias = criterias
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name

    @property
    def criterias(self):
        """Gets the criterias of this SearchCriteriasBody.

        单个日志流的快速查询

        :return: The criterias of this SearchCriteriasBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.GetQuerySearchCriteriasBody`]
        """
        return self._criterias

    @criterias.setter
    def criterias(self, criterias):
        """Sets the criterias of this SearchCriteriasBody.

        单个日志流的快速查询

        :param criterias: The criterias of this SearchCriteriasBody.
        :type criterias: list[:class:`huaweicloudsdklts.v2.GetQuerySearchCriteriasBody`]
        """
        self._criterias = criterias

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this SearchCriteriasBody.

        日志流id

        :return: The log_stream_id of this SearchCriteriasBody.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this SearchCriteriasBody.

        日志流id

        :param log_stream_id: The log_stream_id of this SearchCriteriasBody.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this SearchCriteriasBody.

        日志流名称

        :return: The log_stream_name of this SearchCriteriasBody.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this SearchCriteriasBody.

        日志流名称

        :param log_stream_name: The log_stream_name of this SearchCriteriasBody.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

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
        if not isinstance(other, SearchCriteriasBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
