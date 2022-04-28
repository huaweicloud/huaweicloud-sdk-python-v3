# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerPublicip:

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
        'eip': 'PostPaidServerEip',
        'delete_on_termination': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'eip': 'eip',
        'delete_on_termination': 'delete_on_termination'
    }

    def __init__(self, id=None, eip=None, delete_on_termination=None):
        """PostPaidServerPublicip

        The model defined in huaweicloud sdk

        :param id: 为待创建云服务器分配已有弹性IP时，分配的弹性IP的ID，UUID格式。  约束：只能分配状态（status）为DOWN的弹性IP。
        :type id: str
        :param eip: 
        :type eip: :class:`huaweicloudsdkecs.v2.PostPaidServerEip`
        :param delete_on_termination: 弹性公网IP随实例释放策略。  true：弹性公网IP随实例释放。 false：弹性公网IP不随实例释放。 默认值：false。
        :type delete_on_termination: bool
        """
        
        

        self._id = None
        self._eip = None
        self._delete_on_termination = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if eip is not None:
            self.eip = eip
        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination

    @property
    def id(self):
        """Gets the id of this PostPaidServerPublicip.

        为待创建云服务器分配已有弹性IP时，分配的弹性IP的ID，UUID格式。  约束：只能分配状态（status）为DOWN的弹性IP。

        :return: The id of this PostPaidServerPublicip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostPaidServerPublicip.

        为待创建云服务器分配已有弹性IP时，分配的弹性IP的ID，UUID格式。  约束：只能分配状态（status）为DOWN的弹性IP。

        :param id: The id of this PostPaidServerPublicip.
        :type id: str
        """
        self._id = id

    @property
    def eip(self):
        """Gets the eip of this PostPaidServerPublicip.


        :return: The eip of this PostPaidServerPublicip.
        :rtype: :class:`huaweicloudsdkecs.v2.PostPaidServerEip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this PostPaidServerPublicip.


        :param eip: The eip of this PostPaidServerPublicip.
        :type eip: :class:`huaweicloudsdkecs.v2.PostPaidServerEip`
        """
        self._eip = eip

    @property
    def delete_on_termination(self):
        """Gets the delete_on_termination of this PostPaidServerPublicip.

        弹性公网IP随实例释放策略。  true：弹性公网IP随实例释放。 false：弹性公网IP不随实例释放。 默认值：false。

        :return: The delete_on_termination of this PostPaidServerPublicip.
        :rtype: bool
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        """Sets the delete_on_termination of this PostPaidServerPublicip.

        弹性公网IP随实例释放策略。  true：弹性公网IP随实例释放。 false：弹性公网IP不随实例释放。 默认值：false。

        :param delete_on_termination: The delete_on_termination of this PostPaidServerPublicip.
        :type delete_on_termination: bool
        """
        self._delete_on_termination = delete_on_termination

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
        if not isinstance(other, PostPaidServerPublicip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
