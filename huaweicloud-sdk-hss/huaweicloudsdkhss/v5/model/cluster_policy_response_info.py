# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterPolicyResponseInfo:

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
        'cluster_name': 'str',
        'content': 'object',
        'deploy_content': 'str',
        'parameters': 'str',
        'policy_name': 'str',
        'policy_id': 'str',
        'resources': 'list[Resources]',
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'description': 'str',
        'update_time': 'int',
        'create_time': 'int',
        'image_num': 'int',
        'labels_num': 'int',
        'status': 'str',
        'white_images': 'list[WhiteImageInfo]'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'content': 'content',
        'deploy_content': 'deploy_content',
        'parameters': 'parameters',
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'resources': 'resources',
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'description': 'description',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'image_num': 'image_num',
        'labels_num': 'labels_num',
        'status': 'status',
        'white_images': 'white_images'
    }

    def __init__(self, cluster_id=None, cluster_name=None, content=None, deploy_content=None, parameters=None, policy_name=None, policy_id=None, resources=None, template_id=None, template_name=None, template_type=None, description=None, update_time=None, create_time=None, image_num=None, labels_num=None, status=None, white_images=None):
        r"""ClusterPolicyResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param content: 策略内容
        :type content: object
        :param deploy_content: deploy内容
        :type deploy_content: str
        :param parameters: 参数
        :type parameters: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param resources: 资源
        :type resources: list[:class:`huaweicloudsdkhss.v5.Resources`]
        :param template_id: 模板ID
        :type template_id: str
        :param template_name: 模板名称
        :type template_name: str
        :param template_type: 模板类型
        :type template_type: str
        :param description: 策略描述
        :type description: str
        :param update_time: 更新时间
        :type update_time: int
        :param create_time: 创建时间
        :type create_time: int
        :param image_num: 防护镜像数量
        :type image_num: int
        :param labels_num: 防护标签数量
        :type labels_num: int
        :param status: 状态
        :type status: str
        :param white_images: 白名单镜像
        :type white_images: list[:class:`huaweicloudsdkhss.v5.WhiteImageInfo`]
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._content = None
        self._deploy_content = None
        self._parameters = None
        self._policy_name = None
        self._policy_id = None
        self._resources = None
        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._description = None
        self._update_time = None
        self._create_time = None
        self._image_num = None
        self._labels_num = None
        self._status = None
        self._white_images = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if content is not None:
            self.content = content
        if deploy_content is not None:
            self.deploy_content = deploy_content
        if parameters is not None:
            self.parameters = parameters
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_id is not None:
            self.policy_id = policy_id
        if resources is not None:
            self.resources = resources
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type
        if description is not None:
            self.description = description
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if image_num is not None:
            self.image_num = image_num
        if labels_num is not None:
            self.labels_num = labels_num
        if status is not None:
            self.status = status
        if white_images is not None:
            self.white_images = white_images

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterPolicyResponseInfo.

        集群id

        :return: The cluster_id of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterPolicyResponseInfo.

        集群id

        :param cluster_id: The cluster_id of this ClusterPolicyResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterPolicyResponseInfo.

        集群名称

        :return: The cluster_name of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterPolicyResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClusterPolicyResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def content(self):
        r"""Gets the content of this ClusterPolicyResponseInfo.

        策略内容

        :return: The content of this ClusterPolicyResponseInfo.
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ClusterPolicyResponseInfo.

        策略内容

        :param content: The content of this ClusterPolicyResponseInfo.
        :type content: object
        """
        self._content = content

    @property
    def deploy_content(self):
        r"""Gets the deploy_content of this ClusterPolicyResponseInfo.

        deploy内容

        :return: The deploy_content of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._deploy_content

    @deploy_content.setter
    def deploy_content(self, deploy_content):
        r"""Sets the deploy_content of this ClusterPolicyResponseInfo.

        deploy内容

        :param deploy_content: The deploy_content of this ClusterPolicyResponseInfo.
        :type deploy_content: str
        """
        self._deploy_content = deploy_content

    @property
    def parameters(self):
        r"""Gets the parameters of this ClusterPolicyResponseInfo.

        参数

        :return: The parameters of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ClusterPolicyResponseInfo.

        参数

        :param parameters: The parameters of this ClusterPolicyResponseInfo.
        :type parameters: str
        """
        self._parameters = parameters

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ClusterPolicyResponseInfo.

        策略名称

        :return: The policy_name of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ClusterPolicyResponseInfo.

        策略名称

        :param policy_name: The policy_name of this ClusterPolicyResponseInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ClusterPolicyResponseInfo.

        策略ID

        :return: The policy_id of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ClusterPolicyResponseInfo.

        策略ID

        :param policy_id: The policy_id of this ClusterPolicyResponseInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def resources(self):
        r"""Gets the resources of this ClusterPolicyResponseInfo.

        资源

        :return: The resources of this ClusterPolicyResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.Resources`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ClusterPolicyResponseInfo.

        资源

        :param resources: The resources of this ClusterPolicyResponseInfo.
        :type resources: list[:class:`huaweicloudsdkhss.v5.Resources`]
        """
        self._resources = resources

    @property
    def template_id(self):
        r"""Gets the template_id of this ClusterPolicyResponseInfo.

        模板ID

        :return: The template_id of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ClusterPolicyResponseInfo.

        模板ID

        :param template_id: The template_id of this ClusterPolicyResponseInfo.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        r"""Gets the template_name of this ClusterPolicyResponseInfo.

        模板名称

        :return: The template_name of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ClusterPolicyResponseInfo.

        模板名称

        :param template_name: The template_name of this ClusterPolicyResponseInfo.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this ClusterPolicyResponseInfo.

        模板类型

        :return: The template_type of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ClusterPolicyResponseInfo.

        模板类型

        :param template_type: The template_type of this ClusterPolicyResponseInfo.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def description(self):
        r"""Gets the description of this ClusterPolicyResponseInfo.

        策略描述

        :return: The description of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ClusterPolicyResponseInfo.

        策略描述

        :param description: The description of this ClusterPolicyResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def update_time(self):
        r"""Gets the update_time of this ClusterPolicyResponseInfo.

        更新时间

        :return: The update_time of this ClusterPolicyResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ClusterPolicyResponseInfo.

        更新时间

        :param update_time: The update_time of this ClusterPolicyResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ClusterPolicyResponseInfo.

        创建时间

        :return: The create_time of this ClusterPolicyResponseInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ClusterPolicyResponseInfo.

        创建时间

        :param create_time: The create_time of this ClusterPolicyResponseInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def image_num(self):
        r"""Gets the image_num of this ClusterPolicyResponseInfo.

        防护镜像数量

        :return: The image_num of this ClusterPolicyResponseInfo.
        :rtype: int
        """
        return self._image_num

    @image_num.setter
    def image_num(self, image_num):
        r"""Sets the image_num of this ClusterPolicyResponseInfo.

        防护镜像数量

        :param image_num: The image_num of this ClusterPolicyResponseInfo.
        :type image_num: int
        """
        self._image_num = image_num

    @property
    def labels_num(self):
        r"""Gets the labels_num of this ClusterPolicyResponseInfo.

        防护标签数量

        :return: The labels_num of this ClusterPolicyResponseInfo.
        :rtype: int
        """
        return self._labels_num

    @labels_num.setter
    def labels_num(self, labels_num):
        r"""Sets the labels_num of this ClusterPolicyResponseInfo.

        防护标签数量

        :param labels_num: The labels_num of this ClusterPolicyResponseInfo.
        :type labels_num: int
        """
        self._labels_num = labels_num

    @property
    def status(self):
        r"""Gets the status of this ClusterPolicyResponseInfo.

        状态

        :return: The status of this ClusterPolicyResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterPolicyResponseInfo.

        状态

        :param status: The status of this ClusterPolicyResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def white_images(self):
        r"""Gets the white_images of this ClusterPolicyResponseInfo.

        白名单镜像

        :return: The white_images of this ClusterPolicyResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.WhiteImageInfo`]
        """
        return self._white_images

    @white_images.setter
    def white_images(self, white_images):
        r"""Sets the white_images of this ClusterPolicyResponseInfo.

        白名单镜像

        :param white_images: The white_images of this ClusterPolicyResponseInfo.
        :type white_images: list[:class:`huaweicloudsdkhss.v5.WhiteImageInfo`]
        """
        self._white_images = white_images

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
        if not isinstance(other, ClusterPolicyResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
