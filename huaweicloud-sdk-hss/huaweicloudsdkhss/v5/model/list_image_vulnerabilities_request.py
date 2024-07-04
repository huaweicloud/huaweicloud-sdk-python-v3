# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageVulnerabilitiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'image_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'image_id': 'str',
        'instance_id': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'tag_name': 'str',
        'repair_necessity': 'str',
        'vul_id': 'str',
        'app_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'image_type': 'image_type',
        'offset': 'offset',
        'limit': 'limit',
        'image_id': 'image_id',
        'instance_id': 'instance_id',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'tag_name': 'tag_name',
        'repair_necessity': 'repair_necessity',
        'vul_id': 'vul_id',
        'app_name': 'app_name',
        'type': 'type'
    }

    def __init__(self, region=None, enterprise_project_id=None, image_type=None, offset=None, limit=None, image_id=None, instance_id=None, namespace=None, image_name=None, tag_name=None, repair_necessity=None, vul_id=None, app_name=None, type=None):
        """ListImageVulnerabilitiesRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param image_type: 镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像
        :type image_type: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示数量
        :type limit: int
        :param image_id: 镜像id
        :type image_id: str
        :param instance_id: 企业仓库实例ID，swr共享版无需使用该参数
        :type instance_id: str
        :param namespace: 组织名称
        :type namespace: str
        :param image_name: 镜像名称
        :type image_name: str
        :param tag_name: 镜像版本
        :type tag_name: str
        :param repair_necessity: 危险程度，包含如下3种。   - immediate_repair ：高危。   - delay_repair ：中危。   - not_needed_repair ：低危。
        :type repair_necessity: str
        :param vul_id: 漏洞ID（支持模糊查询）
        :type vul_id: str
        :param app_name: 软件名
        :type app_name: str
        :param type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞
        :type type: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._image_type = None
        self._offset = None
        self._limit = None
        self._image_id = None
        self._instance_id = None
        self._namespace = None
        self._image_name = None
        self._tag_name = None
        self._repair_necessity = None
        self._vul_id = None
        self._app_name = None
        self._type = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.image_type = image_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.image_id = image_id
        if instance_id is not None:
            self.instance_id = instance_id
        self.namespace = namespace
        self.image_name = image_name
        self.tag_name = tag_name
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if vul_id is not None:
            self.vul_id = vul_id
        if app_name is not None:
            self.app_name = app_name
        if type is not None:
            self.type = type

    @property
    def region(self):
        """Gets the region of this ListImageVulnerabilitiesRequest.

        Region ID

        :return: The region of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListImageVulnerabilitiesRequest.

        Region ID

        :param region: The region of this ListImageVulnerabilitiesRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListImageVulnerabilitiesRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListImageVulnerabilitiesRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListImageVulnerabilitiesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_type(self):
        """Gets the image_type of this ListImageVulnerabilitiesRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像

        :return: The image_type of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ListImageVulnerabilitiesRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像

        :param image_type: The image_type of this ListImageVulnerabilitiesRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def offset(self):
        """Gets the offset of this ListImageVulnerabilitiesRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListImageVulnerabilitiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListImageVulnerabilitiesRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListImageVulnerabilitiesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListImageVulnerabilitiesRequest.

        每页显示数量

        :return: The limit of this ListImageVulnerabilitiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListImageVulnerabilitiesRequest.

        每页显示数量

        :param limit: The limit of this ListImageVulnerabilitiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_id(self):
        """Gets the image_id of this ListImageVulnerabilitiesRequest.

        镜像id

        :return: The image_id of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ListImageVulnerabilitiesRequest.

        镜像id

        :param image_id: The image_id of this ListImageVulnerabilitiesRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListImageVulnerabilitiesRequest.

        企业仓库实例ID，swr共享版无需使用该参数

        :return: The instance_id of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListImageVulnerabilitiesRequest.

        企业仓库实例ID，swr共享版无需使用该参数

        :param instance_id: The instance_id of this ListImageVulnerabilitiesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def namespace(self):
        """Gets the namespace of this ListImageVulnerabilitiesRequest.

        组织名称

        :return: The namespace of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListImageVulnerabilitiesRequest.

        组织名称

        :param namespace: The namespace of this ListImageVulnerabilitiesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        """Gets the image_name of this ListImageVulnerabilitiesRequest.

        镜像名称

        :return: The image_name of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ListImageVulnerabilitiesRequest.

        镜像名称

        :param image_name: The image_name of this ListImageVulnerabilitiesRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def tag_name(self):
        """Gets the tag_name of this ListImageVulnerabilitiesRequest.

        镜像版本

        :return: The tag_name of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this ListImageVulnerabilitiesRequest.

        镜像版本

        :param tag_name: The tag_name of this ListImageVulnerabilitiesRequest.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def repair_necessity(self):
        """Gets the repair_necessity of this ListImageVulnerabilitiesRequest.

        危险程度，包含如下3种。   - immediate_repair ：高危。   - delay_repair ：中危。   - not_needed_repair ：低危。

        :return: The repair_necessity of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        """Sets the repair_necessity of this ListImageVulnerabilitiesRequest.

        危险程度，包含如下3种。   - immediate_repair ：高危。   - delay_repair ：中危。   - not_needed_repair ：低危。

        :param repair_necessity: The repair_necessity of this ListImageVulnerabilitiesRequest.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def vul_id(self):
        """Gets the vul_id of this ListImageVulnerabilitiesRequest.

        漏洞ID（支持模糊查询）

        :return: The vul_id of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        """Sets the vul_id of this ListImageVulnerabilitiesRequest.

        漏洞ID（支持模糊查询）

        :param vul_id: The vul_id of this ListImageVulnerabilitiesRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def app_name(self):
        """Gets the app_name of this ListImageVulnerabilitiesRequest.

        软件名

        :return: The app_name of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListImageVulnerabilitiesRequest.

        软件名

        :param app_name: The app_name of this ListImageVulnerabilitiesRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def type(self):
        """Gets the type of this ListImageVulnerabilitiesRequest.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞

        :return: The type of this ListImageVulnerabilitiesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListImageVulnerabilitiesRequest.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -app_vul : 应用漏洞

        :param type: The type of this ListImageVulnerabilitiesRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListImageVulnerabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
