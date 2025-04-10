# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessCatalogTreeNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_catalog_guid': 'str',
        'business_catalog_name': 'str',
        'business_catalog_name_eng': 'str',
        'level': 'str',
        'qualified_name': 'str',
        'ordinal': 'int',
        'child_nodes': 'list[BusinessCatalogTreeNode]',
        'logic_entity_nodes': 'list[LogicEntityNodes]'
    }

    attribute_map = {
        'business_catalog_guid': 'business_catalog_guid',
        'business_catalog_name': 'business_catalog_name',
        'business_catalog_name_eng': 'business_catalog_name_eng',
        'level': 'level',
        'qualified_name': 'qualified_name',
        'ordinal': 'ordinal',
        'child_nodes': 'child_nodes',
        'logic_entity_nodes': 'logic_entity_nodes'
    }

    def __init__(self, business_catalog_guid=None, business_catalog_name=None, business_catalog_name_eng=None, level=None, qualified_name=None, ordinal=None, child_nodes=None, logic_entity_nodes=None):
        r"""BusinessCatalogTreeNode

        The model defined in huaweicloud sdk

        :param business_catalog_guid: 业务资产guid
        :type business_catalog_guid: str
        :param business_catalog_name: 业务资产名称
        :type business_catalog_name: str
        :param business_catalog_name_eng: 业务资产英文名称
        :type business_catalog_name_eng: str
        :param level: 业务资产级别
        :type level: str
        :param qualified_name: 业务资产级唯一限定名称
        :type qualified_name: str
        :param ordinal: 序数
        :type ordinal: int
        :param child_nodes: 子级业务资产列表
        :type child_nodes: list[:class:`huaweicloudsdkdataartsstudio.v1.BusinessCatalogTreeNode`]
        :param logic_entity_nodes: 逻辑实体列表
        :type logic_entity_nodes: list[:class:`huaweicloudsdkdataartsstudio.v1.LogicEntityNodes`]
        """
        
        

        self._business_catalog_guid = None
        self._business_catalog_name = None
        self._business_catalog_name_eng = None
        self._level = None
        self._qualified_name = None
        self._ordinal = None
        self._child_nodes = None
        self._logic_entity_nodes = None
        self.discriminator = None

        if business_catalog_guid is not None:
            self.business_catalog_guid = business_catalog_guid
        if business_catalog_name is not None:
            self.business_catalog_name = business_catalog_name
        if business_catalog_name_eng is not None:
            self.business_catalog_name_eng = business_catalog_name_eng
        if level is not None:
            self.level = level
        if qualified_name is not None:
            self.qualified_name = qualified_name
        if ordinal is not None:
            self.ordinal = ordinal
        if child_nodes is not None:
            self.child_nodes = child_nodes
        if logic_entity_nodes is not None:
            self.logic_entity_nodes = logic_entity_nodes

    @property
    def business_catalog_guid(self):
        r"""Gets the business_catalog_guid of this BusinessCatalogTreeNode.

        业务资产guid

        :return: The business_catalog_guid of this BusinessCatalogTreeNode.
        :rtype: str
        """
        return self._business_catalog_guid

    @business_catalog_guid.setter
    def business_catalog_guid(self, business_catalog_guid):
        r"""Sets the business_catalog_guid of this BusinessCatalogTreeNode.

        业务资产guid

        :param business_catalog_guid: The business_catalog_guid of this BusinessCatalogTreeNode.
        :type business_catalog_guid: str
        """
        self._business_catalog_guid = business_catalog_guid

    @property
    def business_catalog_name(self):
        r"""Gets the business_catalog_name of this BusinessCatalogTreeNode.

        业务资产名称

        :return: The business_catalog_name of this BusinessCatalogTreeNode.
        :rtype: str
        """
        return self._business_catalog_name

    @business_catalog_name.setter
    def business_catalog_name(self, business_catalog_name):
        r"""Sets the business_catalog_name of this BusinessCatalogTreeNode.

        业务资产名称

        :param business_catalog_name: The business_catalog_name of this BusinessCatalogTreeNode.
        :type business_catalog_name: str
        """
        self._business_catalog_name = business_catalog_name

    @property
    def business_catalog_name_eng(self):
        r"""Gets the business_catalog_name_eng of this BusinessCatalogTreeNode.

        业务资产英文名称

        :return: The business_catalog_name_eng of this BusinessCatalogTreeNode.
        :rtype: str
        """
        return self._business_catalog_name_eng

    @business_catalog_name_eng.setter
    def business_catalog_name_eng(self, business_catalog_name_eng):
        r"""Sets the business_catalog_name_eng of this BusinessCatalogTreeNode.

        业务资产英文名称

        :param business_catalog_name_eng: The business_catalog_name_eng of this BusinessCatalogTreeNode.
        :type business_catalog_name_eng: str
        """
        self._business_catalog_name_eng = business_catalog_name_eng

    @property
    def level(self):
        r"""Gets the level of this BusinessCatalogTreeNode.

        业务资产级别

        :return: The level of this BusinessCatalogTreeNode.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this BusinessCatalogTreeNode.

        业务资产级别

        :param level: The level of this BusinessCatalogTreeNode.
        :type level: str
        """
        self._level = level

    @property
    def qualified_name(self):
        r"""Gets the qualified_name of this BusinessCatalogTreeNode.

        业务资产级唯一限定名称

        :return: The qualified_name of this BusinessCatalogTreeNode.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        r"""Sets the qualified_name of this BusinessCatalogTreeNode.

        业务资产级唯一限定名称

        :param qualified_name: The qualified_name of this BusinessCatalogTreeNode.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

    @property
    def ordinal(self):
        r"""Gets the ordinal of this BusinessCatalogTreeNode.

        序数

        :return: The ordinal of this BusinessCatalogTreeNode.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this BusinessCatalogTreeNode.

        序数

        :param ordinal: The ordinal of this BusinessCatalogTreeNode.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def child_nodes(self):
        r"""Gets the child_nodes of this BusinessCatalogTreeNode.

        子级业务资产列表

        :return: The child_nodes of this BusinessCatalogTreeNode.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BusinessCatalogTreeNode`]
        """
        return self._child_nodes

    @child_nodes.setter
    def child_nodes(self, child_nodes):
        r"""Sets the child_nodes of this BusinessCatalogTreeNode.

        子级业务资产列表

        :param child_nodes: The child_nodes of this BusinessCatalogTreeNode.
        :type child_nodes: list[:class:`huaweicloudsdkdataartsstudio.v1.BusinessCatalogTreeNode`]
        """
        self._child_nodes = child_nodes

    @property
    def logic_entity_nodes(self):
        r"""Gets the logic_entity_nodes of this BusinessCatalogTreeNode.

        逻辑实体列表

        :return: The logic_entity_nodes of this BusinessCatalogTreeNode.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.LogicEntityNodes`]
        """
        return self._logic_entity_nodes

    @logic_entity_nodes.setter
    def logic_entity_nodes(self, logic_entity_nodes):
        r"""Sets the logic_entity_nodes of this BusinessCatalogTreeNode.

        逻辑实体列表

        :param logic_entity_nodes: The logic_entity_nodes of this BusinessCatalogTreeNode.
        :type logic_entity_nodes: list[:class:`huaweicloudsdkdataartsstudio.v1.LogicEntityNodes`]
        """
        self._logic_entity_nodes = logic_entity_nodes

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
        if not isinstance(other, BusinessCatalogTreeNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
