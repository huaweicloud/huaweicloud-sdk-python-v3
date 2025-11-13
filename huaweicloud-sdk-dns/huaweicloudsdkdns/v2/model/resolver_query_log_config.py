# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResolverQueryLogConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'lts_group_id': 'str',
        'lts_topic_id': 'str',
        'vpc_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'lts_group_id': 'lts_group_id',
        'lts_topic_id': 'lts_topic_id',
        'vpc_ids': 'vpc_ids'
    }

    def __init__(self, id=None, lts_group_id=None, lts_topic_id=None, vpc_ids=None):
        r"""ResolverQueryLogConfig

        The model defined in huaweicloud sdk

        :param id: 解析器访问日志的ID，UUID形式的一个资源标识。
        :type id: str
        :param lts_group_id: 日志组ID。
        :type lts_group_id: str
        :param lts_topic_id: 日志流ID。
        :type lts_topic_id: str
        :param vpc_ids: 关联的VPC ID列表。
        :type vpc_ids: list[str]
        """
        
        

        self._id = None
        self._lts_group_id = None
        self._lts_topic_id = None
        self._vpc_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if lts_group_id is not None:
            self.lts_group_id = lts_group_id
        if lts_topic_id is not None:
            self.lts_topic_id = lts_topic_id
        if vpc_ids is not None:
            self.vpc_ids = vpc_ids

    @property
    def id(self):
        r"""Gets the id of this ResolverQueryLogConfig.

        解析器访问日志的ID，UUID形式的一个资源标识。

        :return: The id of this ResolverQueryLogConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResolverQueryLogConfig.

        解析器访问日志的ID，UUID形式的一个资源标识。

        :param id: The id of this ResolverQueryLogConfig.
        :type id: str
        """
        self._id = id

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this ResolverQueryLogConfig.

        日志组ID。

        :return: The lts_group_id of this ResolverQueryLogConfig.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this ResolverQueryLogConfig.

        日志组ID。

        :param lts_group_id: The lts_group_id of this ResolverQueryLogConfig.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_topic_id(self):
        r"""Gets the lts_topic_id of this ResolverQueryLogConfig.

        日志流ID。

        :return: The lts_topic_id of this ResolverQueryLogConfig.
        :rtype: str
        """
        return self._lts_topic_id

    @lts_topic_id.setter
    def lts_topic_id(self, lts_topic_id):
        r"""Sets the lts_topic_id of this ResolverQueryLogConfig.

        日志流ID。

        :param lts_topic_id: The lts_topic_id of this ResolverQueryLogConfig.
        :type lts_topic_id: str
        """
        self._lts_topic_id = lts_topic_id

    @property
    def vpc_ids(self):
        r"""Gets the vpc_ids of this ResolverQueryLogConfig.

        关联的VPC ID列表。

        :return: The vpc_ids of this ResolverQueryLogConfig.
        :rtype: list[str]
        """
        return self._vpc_ids

    @vpc_ids.setter
    def vpc_ids(self, vpc_ids):
        r"""Sets the vpc_ids of this ResolverQueryLogConfig.

        关联的VPC ID列表。

        :param vpc_ids: The vpc_ids of this ResolverQueryLogConfig.
        :type vpc_ids: list[str]
        """
        self._vpc_ids = vpc_ids

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
        if not isinstance(other, ResolverQueryLogConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
