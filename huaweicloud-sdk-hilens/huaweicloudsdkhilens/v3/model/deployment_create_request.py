# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentCreateRequest:

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
        'deployment': 'DeploymentRequest',
        'description': 'str',
        'license_quota': 'int',
        'name': 'str',
        'node_ids': 'list[str]',
        'source': 'str',
        'svc_order_id': 'str',
        'tags': 'list[DeploymentTag]',
        'node_tags': 'list[TagRequest]',
        'node_num': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'deployment': 'deployment',
        'description': 'description',
        'license_quota': 'license_quota',
        'name': 'name',
        'node_ids': 'node_ids',
        'source': 'source',
        'svc_order_id': 'svc_order_id',
        'tags': 'tags',
        'node_tags': 'node_tags',
        'node_num': 'node_num'
    }

    def __init__(self, cluster_id=None, deployment=None, description=None, license_quota=None, name=None, node_ids=None, source=None, svc_order_id=None, tags=None, node_tags=None, node_num=None):
        """DeploymentCreateRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 应用部署到指定集群，与node_ids二选一
        :type cluster_id: str
        :param deployment: 
        :type deployment: :class:`huaweicloudsdkhilens.v3.DeploymentRequest`
        :param description: 应用部署描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param license_quota: 本次部署所使用的license额度，配合订单中的计费量纲的实际计费类型，如：视频路数/实例数/QPS。
        :type license_quota: int
        :param name: 应用部署名称，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾
        :type name: str
        :param node_ids: 应用部署到指定节点，与cluster_id二选一
        :type node_ids: list[str]
        :param source: 应用部署来源: HiLens市场(hlm) or aigallery(aig) or 自定义(userdefined)
        :type source: str
        :param svc_order_id: 购买应用管理服务的订单ID。
        :type svc_order_id: str
        :param tags: 部署标签
        :type tags: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
        :param node_tags: 部署节点标签列表，当通过节点标签进行部署的时候，需要下发该字段。
        :type node_tags: list[:class:`huaweicloudsdkhilens.v3.TagRequest`]
        :param node_num: 标签部署的设备数量
        :type node_num: int
        """
        
        

        self._cluster_id = None
        self._deployment = None
        self._description = None
        self._license_quota = None
        self._name = None
        self._node_ids = None
        self._source = None
        self._svc_order_id = None
        self._tags = None
        self._node_tags = None
        self._node_num = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        self.deployment = deployment
        if description is not None:
            self.description = description
        if license_quota is not None:
            self.license_quota = license_quota
        self.name = name
        if node_ids is not None:
            self.node_ids = node_ids
        self.source = source
        if svc_order_id is not None:
            self.svc_order_id = svc_order_id
        if tags is not None:
            self.tags = tags
        if node_tags is not None:
            self.node_tags = node_tags
        if node_num is not None:
            self.node_num = node_num

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeploymentCreateRequest.

        应用部署到指定集群，与node_ids二选一

        :return: The cluster_id of this DeploymentCreateRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeploymentCreateRequest.

        应用部署到指定集群，与node_ids二选一

        :param cluster_id: The cluster_id of this DeploymentCreateRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def deployment(self):
        """Gets the deployment of this DeploymentCreateRequest.

        :return: The deployment of this DeploymentCreateRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.DeploymentRequest`
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this DeploymentCreateRequest.

        :param deployment: The deployment of this DeploymentCreateRequest.
        :type deployment: :class:`huaweicloudsdkhilens.v3.DeploymentRequest`
        """
        self._deployment = deployment

    @property
    def description(self):
        """Gets the description of this DeploymentCreateRequest.

        应用部署描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this DeploymentCreateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentCreateRequest.

        应用部署描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this DeploymentCreateRequest.
        :type description: str
        """
        self._description = description

    @property
    def license_quota(self):
        """Gets the license_quota of this DeploymentCreateRequest.

        本次部署所使用的license额度，配合订单中的计费量纲的实际计费类型，如：视频路数/实例数/QPS。

        :return: The license_quota of this DeploymentCreateRequest.
        :rtype: int
        """
        return self._license_quota

    @license_quota.setter
    def license_quota(self, license_quota):
        """Sets the license_quota of this DeploymentCreateRequest.

        本次部署所使用的license额度，配合订单中的计费量纲的实际计费类型，如：视频路数/实例数/QPS。

        :param license_quota: The license_quota of this DeploymentCreateRequest.
        :type license_quota: int
        """
        self._license_quota = license_quota

    @property
    def name(self):
        """Gets the name of this DeploymentCreateRequest.

        应用部署名称，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾

        :return: The name of this DeploymentCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentCreateRequest.

        应用部署名称，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾

        :param name: The name of this DeploymentCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def node_ids(self):
        """Gets the node_ids of this DeploymentCreateRequest.

        应用部署到指定节点，与cluster_id二选一

        :return: The node_ids of this DeploymentCreateRequest.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this DeploymentCreateRequest.

        应用部署到指定节点，与cluster_id二选一

        :param node_ids: The node_ids of this DeploymentCreateRequest.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def source(self):
        """Gets the source of this DeploymentCreateRequest.

        应用部署来源: HiLens市场(hlm) or aigallery(aig) or 自定义(userdefined)

        :return: The source of this DeploymentCreateRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DeploymentCreateRequest.

        应用部署来源: HiLens市场(hlm) or aigallery(aig) or 自定义(userdefined)

        :param source: The source of this DeploymentCreateRequest.
        :type source: str
        """
        self._source = source

    @property
    def svc_order_id(self):
        """Gets the svc_order_id of this DeploymentCreateRequest.

        购买应用管理服务的订单ID。

        :return: The svc_order_id of this DeploymentCreateRequest.
        :rtype: str
        """
        return self._svc_order_id

    @svc_order_id.setter
    def svc_order_id(self, svc_order_id):
        """Sets the svc_order_id of this DeploymentCreateRequest.

        购买应用管理服务的订单ID。

        :param svc_order_id: The svc_order_id of this DeploymentCreateRequest.
        :type svc_order_id: str
        """
        self._svc_order_id = svc_order_id

    @property
    def tags(self):
        """Gets the tags of this DeploymentCreateRequest.

        部署标签

        :return: The tags of this DeploymentCreateRequest.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DeploymentCreateRequest.

        部署标签

        :param tags: The tags of this DeploymentCreateRequest.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
        """
        self._tags = tags

    @property
    def node_tags(self):
        """Gets the node_tags of this DeploymentCreateRequest.

        部署节点标签列表，当通过节点标签进行部署的时候，需要下发该字段。

        :return: The node_tags of this DeploymentCreateRequest.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TagRequest`]
        """
        return self._node_tags

    @node_tags.setter
    def node_tags(self, node_tags):
        """Sets the node_tags of this DeploymentCreateRequest.

        部署节点标签列表，当通过节点标签进行部署的时候，需要下发该字段。

        :param node_tags: The node_tags of this DeploymentCreateRequest.
        :type node_tags: list[:class:`huaweicloudsdkhilens.v3.TagRequest`]
        """
        self._node_tags = node_tags

    @property
    def node_num(self):
        """Gets the node_num of this DeploymentCreateRequest.

        标签部署的设备数量

        :return: The node_num of this DeploymentCreateRequest.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this DeploymentCreateRequest.

        标签部署的设备数量

        :param node_num: The node_num of this DeploymentCreateRequest.
        :type node_num: int
        """
        self._node_num = node_num

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
        if not isinstance(other, DeploymentCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
