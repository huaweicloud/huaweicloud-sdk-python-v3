# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQueryDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'query_id': 'str',
        'ctime': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'query_id': 'query_id',
        'ctime': 'ctime'
    }

    def __init__(self, cluster_id=None, query_id=None, ctime=None):
        r"""ShowQueryDetailRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param query_id: **参数解释**： 查询ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type query_id: str
        :param ctime: **参数解释**： 采集时间，时间戳。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type ctime: int
        """
        
        

        self._cluster_id = None
        self._query_id = None
        self._ctime = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.query_id = query_id
        if ctime is not None:
            self.ctime = ctime

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowQueryDetailRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ShowQueryDetailRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowQueryDetailRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ShowQueryDetailRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def query_id(self):
        r"""Gets the query_id of this ShowQueryDetailRequest.

        **参数解释**： 查询ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The query_id of this ShowQueryDetailRequest.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this ShowQueryDetailRequest.

        **参数解释**： 查询ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param query_id: The query_id of this ShowQueryDetailRequest.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def ctime(self):
        r"""Gets the ctime of this ShowQueryDetailRequest.

        **参数解释**： 采集时间，时间戳。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The ctime of this ShowQueryDetailRequest.
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        r"""Sets the ctime of this ShowQueryDetailRequest.

        **参数解释**： 采集时间，时间戳。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param ctime: The ctime of this ShowQueryDetailRequest.
        :type ctime: int
        """
        self._ctime = ctime

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
        if not isinstance(other, ShowQueryDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
