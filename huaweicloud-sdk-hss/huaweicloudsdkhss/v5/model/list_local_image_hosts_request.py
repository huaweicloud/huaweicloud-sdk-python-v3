# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLocalImageHostsRequest:

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
        'image_digest': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'host_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'agent_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'image_digest': 'image_digest',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'host_name': 'host_name',
        'offset': 'offset',
        'limit': 'limit',
        'agent_id': 'agent_id'
    }

    def __init__(self, region=None, enterprise_project_id=None, image_digest=None, image_name=None, image_version=None, host_name=None, offset=None, limit=None, agent_id=None):
        r"""ListLocalImageHostsRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param image_digest: 镜像digest
        :type image_digest: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param host_name: 服务器名称
        :type host_name: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param agent_id: Agent Id
        :type agent_id: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._image_digest = None
        self._image_name = None
        self._image_version = None
        self._host_name = None
        self._offset = None
        self._limit = None
        self._agent_id = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_digest is not None:
            self.image_digest = image_digest
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if host_name is not None:
            self.host_name = host_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if agent_id is not None:
            self.agent_id = agent_id

    @property
    def region(self):
        r"""Gets the region of this ListLocalImageHostsRequest.

        Region ID

        :return: The region of this ListLocalImageHostsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListLocalImageHostsRequest.

        Region ID

        :param region: The region of this ListLocalImageHostsRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListLocalImageHostsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListLocalImageHostsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListLocalImageHostsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListLocalImageHostsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_digest(self):
        r"""Gets the image_digest of this ListLocalImageHostsRequest.

        镜像digest

        :return: The image_digest of this ListLocalImageHostsRequest.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this ListLocalImageHostsRequest.

        镜像digest

        :param image_digest: The image_digest of this ListLocalImageHostsRequest.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_name(self):
        r"""Gets the image_name of this ListLocalImageHostsRequest.

        镜像名称

        :return: The image_name of this ListLocalImageHostsRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListLocalImageHostsRequest.

        镜像名称

        :param image_name: The image_name of this ListLocalImageHostsRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListLocalImageHostsRequest.

        镜像版本

        :return: The image_version of this ListLocalImageHostsRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListLocalImageHostsRequest.

        镜像版本

        :param image_version: The image_version of this ListLocalImageHostsRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def host_name(self):
        r"""Gets the host_name of this ListLocalImageHostsRequest.

        服务器名称

        :return: The host_name of this ListLocalImageHostsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListLocalImageHostsRequest.

        服务器名称

        :param host_name: The host_name of this ListLocalImageHostsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def offset(self):
        r"""Gets the offset of this ListLocalImageHostsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListLocalImageHostsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLocalImageHostsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListLocalImageHostsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLocalImageHostsRequest.

        每页显示个数

        :return: The limit of this ListLocalImageHostsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLocalImageHostsRequest.

        每页显示个数

        :param limit: The limit of this ListLocalImageHostsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ListLocalImageHostsRequest.

        Agent Id

        :return: The agent_id of this ListLocalImageHostsRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ListLocalImageHostsRequest.

        Agent Id

        :param agent_id: The agent_id of this ListLocalImageHostsRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

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
        if not isinstance(other, ListLocalImageHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
