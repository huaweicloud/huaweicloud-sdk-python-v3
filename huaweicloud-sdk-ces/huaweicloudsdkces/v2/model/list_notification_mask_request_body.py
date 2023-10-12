# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationMaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation_type': 'ListRelationType',
        'relation_ids': 'list[str]',
        'mask_id': 'str',
        'mask_name': 'str',
        'mask_status': 'str',
        'resource_id': 'str',
        'namespace': 'str',
        'dimensions': 'list[Dimension2]'
    }

    attribute_map = {
        'relation_type': 'relation_type',
        'relation_ids': 'relation_ids',
        'mask_id': 'mask_id',
        'mask_name': 'mask_name',
        'mask_status': 'mask_status',
        'resource_id': 'resource_id',
        'namespace': 'namespace',
        'dimensions': 'dimensions'
    }

    def __init__(self, relation_type=None, relation_ids=None, mask_id=None, mask_name=None, mask_status=None, resource_id=None, namespace=None, dimensions=None):
        """ListNotificationMaskRequestBody

        The model defined in huaweicloud sdk

        :param relation_type: 
        :type relation_type: :class:`huaweicloudsdkces.v2.ListRelationType`
        :param relation_ids: 关联编号（目前是告警规则ID）
        :type relation_ids: list[str]
        :param mask_id: 屏蔽规则ID,可选
        :type mask_id: str
        :param mask_name: 屏蔽规则名称,可选，只能为字母、数字、汉字、-、_，最大长度为64
        :type mask_name: str
        :param mask_status: 屏蔽状态,可选。MASK_EFFECTIVE：已生效，MASK_INEFFECTIVE：未生效。
        :type mask_status: str
        :param resource_id: 资源维度值,提供一个维度的资源ID即可,可选
        :type resource_id: str
        :param namespace: 查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)
        :type namespace: str
        :param dimensions: 资源的维度信息
        :type dimensions: list[:class:`huaweicloudsdkces.v2.Dimension2`]
        """
        
        

        self._relation_type = None
        self._relation_ids = None
        self._mask_id = None
        self._mask_name = None
        self._mask_status = None
        self._resource_id = None
        self._namespace = None
        self._dimensions = None
        self.discriminator = None

        self.relation_type = relation_type
        self.relation_ids = relation_ids
        if mask_id is not None:
            self.mask_id = mask_id
        if mask_name is not None:
            self.mask_name = mask_name
        if mask_status is not None:
            self.mask_status = mask_status
        if resource_id is not None:
            self.resource_id = resource_id
        if namespace is not None:
            self.namespace = namespace
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def relation_type(self):
        """Gets the relation_type of this ListNotificationMaskRequestBody.

        :return: The relation_type of this ListNotificationMaskRequestBody.
        :rtype: :class:`huaweicloudsdkces.v2.ListRelationType`
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this ListNotificationMaskRequestBody.

        :param relation_type: The relation_type of this ListNotificationMaskRequestBody.
        :type relation_type: :class:`huaweicloudsdkces.v2.ListRelationType`
        """
        self._relation_type = relation_type

    @property
    def relation_ids(self):
        """Gets the relation_ids of this ListNotificationMaskRequestBody.

        关联编号（目前是告警规则ID）

        :return: The relation_ids of this ListNotificationMaskRequestBody.
        :rtype: list[str]
        """
        return self._relation_ids

    @relation_ids.setter
    def relation_ids(self, relation_ids):
        """Sets the relation_ids of this ListNotificationMaskRequestBody.

        关联编号（目前是告警规则ID）

        :param relation_ids: The relation_ids of this ListNotificationMaskRequestBody.
        :type relation_ids: list[str]
        """
        self._relation_ids = relation_ids

    @property
    def mask_id(self):
        """Gets the mask_id of this ListNotificationMaskRequestBody.

        屏蔽规则ID,可选

        :return: The mask_id of this ListNotificationMaskRequestBody.
        :rtype: str
        """
        return self._mask_id

    @mask_id.setter
    def mask_id(self, mask_id):
        """Sets the mask_id of this ListNotificationMaskRequestBody.

        屏蔽规则ID,可选

        :param mask_id: The mask_id of this ListNotificationMaskRequestBody.
        :type mask_id: str
        """
        self._mask_id = mask_id

    @property
    def mask_name(self):
        """Gets the mask_name of this ListNotificationMaskRequestBody.

        屏蔽规则名称,可选，只能为字母、数字、汉字、-、_，最大长度为64

        :return: The mask_name of this ListNotificationMaskRequestBody.
        :rtype: str
        """
        return self._mask_name

    @mask_name.setter
    def mask_name(self, mask_name):
        """Sets the mask_name of this ListNotificationMaskRequestBody.

        屏蔽规则名称,可选，只能为字母、数字、汉字、-、_，最大长度为64

        :param mask_name: The mask_name of this ListNotificationMaskRequestBody.
        :type mask_name: str
        """
        self._mask_name = mask_name

    @property
    def mask_status(self):
        """Gets the mask_status of this ListNotificationMaskRequestBody.

        屏蔽状态,可选。MASK_EFFECTIVE：已生效，MASK_INEFFECTIVE：未生效。

        :return: The mask_status of this ListNotificationMaskRequestBody.
        :rtype: str
        """
        return self._mask_status

    @mask_status.setter
    def mask_status(self, mask_status):
        """Sets the mask_status of this ListNotificationMaskRequestBody.

        屏蔽状态,可选。MASK_EFFECTIVE：已生效，MASK_INEFFECTIVE：未生效。

        :param mask_status: The mask_status of this ListNotificationMaskRequestBody.
        :type mask_status: str
        """
        self._mask_status = mask_status

    @property
    def resource_id(self):
        """Gets the resource_id of this ListNotificationMaskRequestBody.

        资源维度值,提供一个维度的资源ID即可,可选

        :return: The resource_id of this ListNotificationMaskRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListNotificationMaskRequestBody.

        资源维度值,提供一个维度的资源ID即可,可选

        :param resource_id: The resource_id of this ListNotificationMaskRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def namespace(self):
        """Gets the namespace of this ListNotificationMaskRequestBody.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :return: The namespace of this ListNotificationMaskRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListNotificationMaskRequestBody.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :param namespace: The namespace of this ListNotificationMaskRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        """Gets the dimensions of this ListNotificationMaskRequestBody.

        资源的维度信息

        :return: The dimensions of this ListNotificationMaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Dimension2`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ListNotificationMaskRequestBody.

        资源的维度信息

        :param dimensions: The dimensions of this ListNotificationMaskRequestBody.
        :type dimensions: list[:class:`huaweicloudsdkces.v2.Dimension2`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, ListNotificationMaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
