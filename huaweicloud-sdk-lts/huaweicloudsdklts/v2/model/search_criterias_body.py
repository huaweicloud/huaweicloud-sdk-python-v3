# coding: utf-8

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
        'log_stream_name': 'str',
        'search_type': 'str'
    }

    attribute_map = {
        'criterias': 'criterias',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'search_type': 'search_type'
    }

    def __init__(self, criterias=None, log_stream_id=None, log_stream_name=None, search_type=None):
        r"""SearchCriteriasBody

        The model defined in huaweicloud sdk

        :param criterias: 单个日志流的快速查询
        :type criterias: list[:class:`huaweicloudsdklts.v2.GetQuerySearchCriteriasBody`]
        :param log_stream_id: 日志流id
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param search_type: **参数解释：** 快速查询类型。 **取值范围：** - ORIGINALLOG：原始日志 - VISUALIZATION：可视化日志
        :type search_type: str
        """
        
        

        self._criterias = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._search_type = None
        self.discriminator = None

        self.criterias = criterias
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if search_type is not None:
            self.search_type = search_type

    @property
    def criterias(self):
        r"""Gets the criterias of this SearchCriteriasBody.

        单个日志流的快速查询

        :return: The criterias of this SearchCriteriasBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.GetQuerySearchCriteriasBody`]
        """
        return self._criterias

    @criterias.setter
    def criterias(self, criterias):
        r"""Sets the criterias of this SearchCriteriasBody.

        单个日志流的快速查询

        :param criterias: The criterias of this SearchCriteriasBody.
        :type criterias: list[:class:`huaweicloudsdklts.v2.GetQuerySearchCriteriasBody`]
        """
        self._criterias = criterias

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this SearchCriteriasBody.

        日志流id

        :return: The log_stream_id of this SearchCriteriasBody.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this SearchCriteriasBody.

        日志流id

        :param log_stream_id: The log_stream_id of this SearchCriteriasBody.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this SearchCriteriasBody.

        日志流名称

        :return: The log_stream_name of this SearchCriteriasBody.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this SearchCriteriasBody.

        日志流名称

        :param log_stream_name: The log_stream_name of this SearchCriteriasBody.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def search_type(self):
        r"""Gets the search_type of this SearchCriteriasBody.

        **参数解释：** 快速查询类型。 **取值范围：** - ORIGINALLOG：原始日志 - VISUALIZATION：可视化日志

        :return: The search_type of this SearchCriteriasBody.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this SearchCriteriasBody.

        **参数解释：** 快速查询类型。 **取值范围：** - ORIGINALLOG：原始日志 - VISUALIZATION：可视化日志

        :param search_type: The search_type of this SearchCriteriasBody.
        :type search_type: str
        """
        self._search_type = search_type

    def to_dict(self):
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
        if not isinstance(other, SearchCriteriasBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
