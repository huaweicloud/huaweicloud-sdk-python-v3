# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataSourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_sources': 'list[ExtDataSource]',
        'project_id': 'str',
        'cluster_id': 'str',
        'type': 'str',
        'count': 'int'
    }

    attribute_map = {
        'data_sources': 'data_sources',
        'project_id': 'project_id',
        'cluster_id': 'cluster_id',
        'type': 'type',
        'count': 'count'
    }

    def __init__(self, data_sources=None, project_id=None, cluster_id=None, type=None, count=None):
        r"""ListDataSourceResponse

        The model defined in huaweicloud sdk

        :param data_sources: **参数解释**： 数据源列表。 **取值范围**： 不涉及。
        :type data_sources: list[:class:`huaweicloudsdkdws.v2.ExtDataSource`]
        :param project_id: **参数解释**： 项目ID。 **取值范围**： 不涉及。
        :type project_id: str
        :param cluster_id: **参数解释**： 集群ID。 **取值范围**： 36位UUID。
        :type cluster_id: str
        :param type: **参数解释**： 数据源类型。 **取值范围**： 不涉及。
        :type type: str
        :param count: **参数解释**： 总数。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListDataSourceResponse, self).__init__()

        self._data_sources = None
        self._project_id = None
        self._cluster_id = None
        self._type = None
        self._count = None
        self.discriminator = None

        if data_sources is not None:
            self.data_sources = data_sources
        if project_id is not None:
            self.project_id = project_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if type is not None:
            self.type = type
        if count is not None:
            self.count = count

    @property
    def data_sources(self):
        r"""Gets the data_sources of this ListDataSourceResponse.

        **参数解释**： 数据源列表。 **取值范围**： 不涉及。

        :return: The data_sources of this ListDataSourceResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ExtDataSource`]
        """
        return self._data_sources

    @data_sources.setter
    def data_sources(self, data_sources):
        r"""Sets the data_sources of this ListDataSourceResponse.

        **参数解释**： 数据源列表。 **取值范围**： 不涉及。

        :param data_sources: The data_sources of this ListDataSourceResponse.
        :type data_sources: list[:class:`huaweicloudsdkdws.v2.ExtDataSource`]
        """
        self._data_sources = data_sources

    @property
    def project_id(self):
        r"""Gets the project_id of this ListDataSourceResponse.

        **参数解释**： 项目ID。 **取值范围**： 不涉及。

        :return: The project_id of this ListDataSourceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListDataSourceResponse.

        **参数解释**： 项目ID。 **取值范围**： 不涉及。

        :param project_id: The project_id of this ListDataSourceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListDataSourceResponse.

        **参数解释**： 集群ID。 **取值范围**： 36位UUID。

        :return: The cluster_id of this ListDataSourceResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListDataSourceResponse.

        **参数解释**： 集群ID。 **取值范围**： 36位UUID。

        :param cluster_id: The cluster_id of this ListDataSourceResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def type(self):
        r"""Gets the type of this ListDataSourceResponse.

        **参数解释**： 数据源类型。 **取值范围**： 不涉及。

        :return: The type of this ListDataSourceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDataSourceResponse.

        **参数解释**： 数据源类型。 **取值范围**： 不涉及。

        :param type: The type of this ListDataSourceResponse.
        :type type: str
        """
        self._type = type

    @property
    def count(self):
        r"""Gets the count of this ListDataSourceResponse.

        **参数解释**： 总数。 **取值范围**： 不涉及。

        :return: The count of this ListDataSourceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListDataSourceResponse.

        **参数解释**： 总数。 **取值范围**： 不涉及。

        :param count: The count of this ListDataSourceResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListDataSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
