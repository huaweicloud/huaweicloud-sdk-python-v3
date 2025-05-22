# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LockNodeScaledownRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'node_list': 'list[str]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'node_list': 'nodeList'
    }

    def __init__(self, api_version=None, kind=None, node_list=None):
        r"""LockNodeScaledownRequestBody

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**： API版本，固定值“v3”。 **约束限制**： 不涉及 **取值范围**： 只能为固定值“v3”。 **默认取值**： 不涉及
        :type api_version: str
        :param kind: **参数解释**： API版本，固定值“List”。 **约束限制**： 不涉及 **取值范围**： 只能为固定值“v3”。 **默认取值**： 不涉及
        :type kind: str
        :param node_list: **参数解释**： 需要关闭缩容保护的节点ID列表，节点ID获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及
        :type node_list: list[str]
        """
        
        

        self._api_version = None
        self._kind = None
        self._node_list = None
        self.discriminator = None

        self.api_version = api_version
        self.kind = kind
        if node_list is not None:
            self.node_list = node_list

    @property
    def api_version(self):
        r"""Gets the api_version of this LockNodeScaledownRequestBody.

        **参数解释**： API版本，固定值“v3”。 **约束限制**： 不涉及 **取值范围**： 只能为固定值“v3”。 **默认取值**： 不涉及

        :return: The api_version of this LockNodeScaledownRequestBody.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this LockNodeScaledownRequestBody.

        **参数解释**： API版本，固定值“v3”。 **约束限制**： 不涉及 **取值范围**： 只能为固定值“v3”。 **默认取值**： 不涉及

        :param api_version: The api_version of this LockNodeScaledownRequestBody.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this LockNodeScaledownRequestBody.

        **参数解释**： API版本，固定值“List”。 **约束限制**： 不涉及 **取值范围**： 只能为固定值“v3”。 **默认取值**： 不涉及

        :return: The kind of this LockNodeScaledownRequestBody.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this LockNodeScaledownRequestBody.

        **参数解释**： API版本，固定值“List”。 **约束限制**： 不涉及 **取值范围**： 只能为固定值“v3”。 **默认取值**： 不涉及

        :param kind: The kind of this LockNodeScaledownRequestBody.
        :type kind: str
        """
        self._kind = kind

    @property
    def node_list(self):
        r"""Gets the node_list of this LockNodeScaledownRequestBody.

        **参数解释**： 需要关闭缩容保护的节点ID列表，节点ID获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及

        :return: The node_list of this LockNodeScaledownRequestBody.
        :rtype: list[str]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this LockNodeScaledownRequestBody.

        **参数解释**： 需要关闭缩容保护的节点ID列表，节点ID获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 不涉及

        :param node_list: The node_list of this LockNodeScaledownRequestBody.
        :type node_list: list[str]
        """
        self._node_list = node_list

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
        if not isinstance(other, LockNodeScaledownRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
