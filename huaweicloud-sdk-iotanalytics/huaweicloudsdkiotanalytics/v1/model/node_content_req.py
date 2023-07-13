# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeContentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'sqllist': 'list[str]'
    }

    attribute_map = {
        'site_id': 'site_id',
        'sqllist': 'sqllist'
    }

    def __init__(self, site_id=None, sqllist=None):
        """NodeContentReq

        The model defined in huaweicloud sdk

        :param site_id: 节点实例ID
        :type site_id: str
        :param sqllist: SQL列表，将指定边缘平台节点的数字孪生模型实例数据转发到中心平台节点。
        :type sqllist: list[str]
        """
        
        

        self._site_id = None
        self._sqllist = None
        self.discriminator = None

        self.site_id = site_id
        self.sqllist = sqllist

    @property
    def site_id(self):
        """Gets the site_id of this NodeContentReq.

        节点实例ID

        :return: The site_id of this NodeContentReq.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this NodeContentReq.

        节点实例ID

        :param site_id: The site_id of this NodeContentReq.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def sqllist(self):
        """Gets the sqllist of this NodeContentReq.

        SQL列表，将指定边缘平台节点的数字孪生模型实例数据转发到中心平台节点。

        :return: The sqllist of this NodeContentReq.
        :rtype: list[str]
        """
        return self._sqllist

    @sqllist.setter
    def sqllist(self, sqllist):
        """Sets the sqllist of this NodeContentReq.

        SQL列表，将指定边缘平台节点的数字孪生模型实例数据转发到中心平台节点。

        :param sqllist: The sqllist of this NodeContentReq.
        :type sqllist: list[str]
        """
        self._sqllist = sqllist

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
        if not isinstance(other, NodeContentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
