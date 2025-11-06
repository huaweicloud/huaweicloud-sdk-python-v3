# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggrPrometheusInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'prometheus_ids': 'list[str]',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'prometheus_ids': 'prometheusIds',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, project_id=None, prometheus_ids=None, id=None, name=None):
        r"""AggrPrometheusInfo

        The model defined in huaweicloud sdk

        :param project_id: 被聚合的账号的projectid。
        :type project_id: str
        :param prometheus_ids: 被聚合的账号下的普罗ID列表。
        :type prometheus_ids: list[str]
        :param id: 被聚合的账号id。
        :type id: str
        :param name: 被聚合的账号名称。
        :type name: str
        """
        
        

        self._project_id = None
        self._prometheus_ids = None
        self._id = None
        self._name = None
        self.discriminator = None

        self.project_id = project_id
        self.prometheus_ids = prometheus_ids
        self.id = id
        self.name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this AggrPrometheusInfo.

        被聚合的账号的projectid。

        :return: The project_id of this AggrPrometheusInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AggrPrometheusInfo.

        被聚合的账号的projectid。

        :param project_id: The project_id of this AggrPrometheusInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def prometheus_ids(self):
        r"""Gets the prometheus_ids of this AggrPrometheusInfo.

        被聚合的账号下的普罗ID列表。

        :return: The prometheus_ids of this AggrPrometheusInfo.
        :rtype: list[str]
        """
        return self._prometheus_ids

    @prometheus_ids.setter
    def prometheus_ids(self, prometheus_ids):
        r"""Sets the prometheus_ids of this AggrPrometheusInfo.

        被聚合的账号下的普罗ID列表。

        :param prometheus_ids: The prometheus_ids of this AggrPrometheusInfo.
        :type prometheus_ids: list[str]
        """
        self._prometheus_ids = prometheus_ids

    @property
    def id(self):
        r"""Gets the id of this AggrPrometheusInfo.

        被聚合的账号id。

        :return: The id of this AggrPrometheusInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AggrPrometheusInfo.

        被聚合的账号id。

        :param id: The id of this AggrPrometheusInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AggrPrometheusInfo.

        被聚合的账号名称。

        :return: The name of this AggrPrometheusInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AggrPrometheusInfo.

        被聚合的账号名称。

        :param name: The name of this AggrPrometheusInfo.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AggrPrometheusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
