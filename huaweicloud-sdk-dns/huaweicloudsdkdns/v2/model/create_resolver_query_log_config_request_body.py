# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResolverQueryLogConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lts_group_id': 'str',
        'lts_topic_id': 'str',
        'vpc': 'Vpc'
    }

    attribute_map = {
        'lts_group_id': 'lts_group_id',
        'lts_topic_id': 'lts_topic_id',
        'vpc': 'vpc'
    }

    def __init__(self, lts_group_id=None, lts_topic_id=None, vpc=None):
        r"""CreateResolverQueryLogConfigRequestBody

        The model defined in huaweicloud sdk

        :param lts_group_id: 日志组ID。
        :type lts_group_id: str
        :param lts_topic_id: 日志流ID。
        :type lts_topic_id: str
        :param vpc: 
        :type vpc: :class:`huaweicloudsdkdns.v2.Vpc`
        """
        
        

        self._lts_group_id = None
        self._lts_topic_id = None
        self._vpc = None
        self.discriminator = None

        self.lts_group_id = lts_group_id
        self.lts_topic_id = lts_topic_id
        self.vpc = vpc

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this CreateResolverQueryLogConfigRequestBody.

        日志组ID。

        :return: The lts_group_id of this CreateResolverQueryLogConfigRequestBody.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this CreateResolverQueryLogConfigRequestBody.

        日志组ID。

        :param lts_group_id: The lts_group_id of this CreateResolverQueryLogConfigRequestBody.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_topic_id(self):
        r"""Gets the lts_topic_id of this CreateResolverQueryLogConfigRequestBody.

        日志流ID。

        :return: The lts_topic_id of this CreateResolverQueryLogConfigRequestBody.
        :rtype: str
        """
        return self._lts_topic_id

    @lts_topic_id.setter
    def lts_topic_id(self, lts_topic_id):
        r"""Sets the lts_topic_id of this CreateResolverQueryLogConfigRequestBody.

        日志流ID。

        :param lts_topic_id: The lts_topic_id of this CreateResolverQueryLogConfigRequestBody.
        :type lts_topic_id: str
        """
        self._lts_topic_id = lts_topic_id

    @property
    def vpc(self):
        r"""Gets the vpc of this CreateResolverQueryLogConfigRequestBody.

        :return: The vpc of this CreateResolverQueryLogConfigRequestBody.
        :rtype: :class:`huaweicloudsdkdns.v2.Vpc`
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this CreateResolverQueryLogConfigRequestBody.

        :param vpc: The vpc of this CreateResolverQueryLogConfigRequestBody.
        :type vpc: :class:`huaweicloudsdkdns.v2.Vpc`
        """
        self._vpc = vpc

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
        if not isinstance(other, CreateResolverQueryLogConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
