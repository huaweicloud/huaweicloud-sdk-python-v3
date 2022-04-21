# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_orgs': 'list[NodeOrgs]',
        'publicips': 'list[IefNodeinfo]',
        'is_delete_org': 'bool'
    }

    attribute_map = {
        'node_orgs': 'node_orgs',
        'publicips': 'publicips',
        'is_delete_org': 'is_delete_org'
    }

    def __init__(self, node_orgs=None, publicips=None, is_delete_org=None):
        """UpdateInstanceRequestBody

        The model defined in huaweicloud sdk

        :param node_orgs: 添加节点的组织列表
        :type node_orgs: list[:class:`huaweicloudsdkbcs.v2.NodeOrgs`]
        :param publicips: ief添加组织时，ief节点信息。绑定模式的IEF服务，新增组织时，该字段必填
        :type publicips: list[:class:`huaweicloudsdkbcs.v2.IefNodeinfo`]
        :param is_delete_org: 是否是删除组织
        :type is_delete_org: bool
        """
        
        

        self._node_orgs = None
        self._publicips = None
        self._is_delete_org = None
        self.discriminator = None

        self.node_orgs = node_orgs
        if publicips is not None:
            self.publicips = publicips
        if is_delete_org is not None:
            self.is_delete_org = is_delete_org

    @property
    def node_orgs(self):
        """Gets the node_orgs of this UpdateInstanceRequestBody.

        添加节点的组织列表

        :return: The node_orgs of this UpdateInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.NodeOrgs`]
        """
        return self._node_orgs

    @node_orgs.setter
    def node_orgs(self, node_orgs):
        """Sets the node_orgs of this UpdateInstanceRequestBody.

        添加节点的组织列表

        :param node_orgs: The node_orgs of this UpdateInstanceRequestBody.
        :type node_orgs: list[:class:`huaweicloudsdkbcs.v2.NodeOrgs`]
        """
        self._node_orgs = node_orgs

    @property
    def publicips(self):
        """Gets the publicips of this UpdateInstanceRequestBody.

        ief添加组织时，ief节点信息。绑定模式的IEF服务，新增组织时，该字段必填

        :return: The publicips of this UpdateInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.IefNodeinfo`]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        """Sets the publicips of this UpdateInstanceRequestBody.

        ief添加组织时，ief节点信息。绑定模式的IEF服务，新增组织时，该字段必填

        :param publicips: The publicips of this UpdateInstanceRequestBody.
        :type publicips: list[:class:`huaweicloudsdkbcs.v2.IefNodeinfo`]
        """
        self._publicips = publicips

    @property
    def is_delete_org(self):
        """Gets the is_delete_org of this UpdateInstanceRequestBody.

        是否是删除组织

        :return: The is_delete_org of this UpdateInstanceRequestBody.
        :rtype: bool
        """
        return self._is_delete_org

    @is_delete_org.setter
    def is_delete_org(self, is_delete_org):
        """Sets the is_delete_org of this UpdateInstanceRequestBody.

        是否是删除组织

        :param is_delete_org: The is_delete_org of this UpdateInstanceRequestBody.
        :type is_delete_org: bool
        """
        self._is_delete_org = is_delete_org

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
        if not isinstance(other, UpdateInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
