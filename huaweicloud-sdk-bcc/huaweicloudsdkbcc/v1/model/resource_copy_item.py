# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceCopyItem:

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
        'copy_id': 'str',
        'copy_name': 'str',
        'copy_type': 'str',
        'region_id': 'str',
        'az_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'ep_id': 'str',
        'ep_name': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'vault_id': 'str',
        'vault_name': 'str',
        'resource_id': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'copy_id': 'copy_id',
        'copy_name': 'copy_name',
        'copy_type': 'copy_type',
        'region_id': 'region_id',
        'az_id': 'az_id',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'ep_id': 'ep_id',
        'ep_name': 'ep_name',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'vault_id': 'vault_id',
        'vault_name': 'vault_name',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name'
    }

    def __init__(self, id=None, copy_id=None, copy_name=None, copy_type=None, region_id=None, az_id=None, project_id=None, project_name=None, ep_id=None, ep_name=None, status=None, begin_time=None, end_time=None, vault_id=None, vault_name=None, resource_id=None, resource_name=None):
        r"""ResourceCopyItem

        The model defined in huaweicloud sdk

        :param id: 副本ID
        :type id: str
        :param copy_id: 源服务的备份ID
        :type copy_id: str
        :param copy_name: 副本名称
        :type copy_name: str
        :param copy_type: 备份类型
        :type copy_type: str
        :param region_id: 区域ID
        :type region_id: str
        :param az_id: 可用区ID
        :type az_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param ep_id: 企业项目ID
        :type ep_id: str
        :param ep_name: 企业项目名称
        :type ep_name: str
        :param status: 副本当前状态
        :type status: str
        :param begin_time: 备份开始时间
        :type begin_time: str
        :param end_time: 备份结束时间
        :type end_time: str
        :param vault_id: CBR存储库ID
        :type vault_id: str
        :param vault_name: CBR存储库名称
        :type vault_name: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        """
        
        

        self._id = None
        self._copy_id = None
        self._copy_name = None
        self._copy_type = None
        self._region_id = None
        self._az_id = None
        self._project_id = None
        self._project_name = None
        self._ep_id = None
        self._ep_name = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._vault_id = None
        self._vault_name = None
        self._resource_id = None
        self._resource_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if copy_id is not None:
            self.copy_id = copy_id
        if copy_name is not None:
            self.copy_name = copy_name
        if copy_type is not None:
            self.copy_type = copy_type
        if region_id is not None:
            self.region_id = region_id
        if az_id is not None:
            self.az_id = az_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if ep_id is not None:
            self.ep_id = ep_id
        if ep_name is not None:
            self.ep_name = ep_name
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if vault_id is not None:
            self.vault_id = vault_id
        if vault_name is not None:
            self.vault_name = vault_name
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def id(self):
        r"""Gets the id of this ResourceCopyItem.

        副本ID

        :return: The id of this ResourceCopyItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResourceCopyItem.

        副本ID

        :param id: The id of this ResourceCopyItem.
        :type id: str
        """
        self._id = id

    @property
    def copy_id(self):
        r"""Gets the copy_id of this ResourceCopyItem.

        源服务的备份ID

        :return: The copy_id of this ResourceCopyItem.
        :rtype: str
        """
        return self._copy_id

    @copy_id.setter
    def copy_id(self, copy_id):
        r"""Sets the copy_id of this ResourceCopyItem.

        源服务的备份ID

        :param copy_id: The copy_id of this ResourceCopyItem.
        :type copy_id: str
        """
        self._copy_id = copy_id

    @property
    def copy_name(self):
        r"""Gets the copy_name of this ResourceCopyItem.

        副本名称

        :return: The copy_name of this ResourceCopyItem.
        :rtype: str
        """
        return self._copy_name

    @copy_name.setter
    def copy_name(self, copy_name):
        r"""Sets the copy_name of this ResourceCopyItem.

        副本名称

        :param copy_name: The copy_name of this ResourceCopyItem.
        :type copy_name: str
        """
        self._copy_name = copy_name

    @property
    def copy_type(self):
        r"""Gets the copy_type of this ResourceCopyItem.

        备份类型

        :return: The copy_type of this ResourceCopyItem.
        :rtype: str
        """
        return self._copy_type

    @copy_type.setter
    def copy_type(self, copy_type):
        r"""Sets the copy_type of this ResourceCopyItem.

        备份类型

        :param copy_type: The copy_type of this ResourceCopyItem.
        :type copy_type: str
        """
        self._copy_type = copy_type

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceCopyItem.

        区域ID

        :return: The region_id of this ResourceCopyItem.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceCopyItem.

        区域ID

        :param region_id: The region_id of this ResourceCopyItem.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def az_id(self):
        r"""Gets the az_id of this ResourceCopyItem.

        可用区ID

        :return: The az_id of this ResourceCopyItem.
        :rtype: str
        """
        return self._az_id

    @az_id.setter
    def az_id(self, az_id):
        r"""Sets the az_id of this ResourceCopyItem.

        可用区ID

        :param az_id: The az_id of this ResourceCopyItem.
        :type az_id: str
        """
        self._az_id = az_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ResourceCopyItem.

        项目ID

        :return: The project_id of this ResourceCopyItem.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ResourceCopyItem.

        项目ID

        :param project_id: The project_id of this ResourceCopyItem.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ResourceCopyItem.

        项目名称

        :return: The project_name of this ResourceCopyItem.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ResourceCopyItem.

        项目名称

        :param project_name: The project_name of this ResourceCopyItem.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def ep_id(self):
        r"""Gets the ep_id of this ResourceCopyItem.

        企业项目ID

        :return: The ep_id of this ResourceCopyItem.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this ResourceCopyItem.

        企业项目ID

        :param ep_id: The ep_id of this ResourceCopyItem.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def ep_name(self):
        r"""Gets the ep_name of this ResourceCopyItem.

        企业项目名称

        :return: The ep_name of this ResourceCopyItem.
        :rtype: str
        """
        return self._ep_name

    @ep_name.setter
    def ep_name(self, ep_name):
        r"""Sets the ep_name of this ResourceCopyItem.

        企业项目名称

        :param ep_name: The ep_name of this ResourceCopyItem.
        :type ep_name: str
        """
        self._ep_name = ep_name

    @property
    def status(self):
        r"""Gets the status of this ResourceCopyItem.

        副本当前状态

        :return: The status of this ResourceCopyItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResourceCopyItem.

        副本当前状态

        :param status: The status of this ResourceCopyItem.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ResourceCopyItem.

        备份开始时间

        :return: The begin_time of this ResourceCopyItem.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ResourceCopyItem.

        备份开始时间

        :param begin_time: The begin_time of this ResourceCopyItem.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ResourceCopyItem.

        备份结束时间

        :return: The end_time of this ResourceCopyItem.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ResourceCopyItem.

        备份结束时间

        :param end_time: The end_time of this ResourceCopyItem.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def vault_id(self):
        r"""Gets the vault_id of this ResourceCopyItem.

        CBR存储库ID

        :return: The vault_id of this ResourceCopyItem.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this ResourceCopyItem.

        CBR存储库ID

        :param vault_id: The vault_id of this ResourceCopyItem.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def vault_name(self):
        r"""Gets the vault_name of this ResourceCopyItem.

        CBR存储库名称

        :return: The vault_name of this ResourceCopyItem.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        r"""Sets the vault_name of this ResourceCopyItem.

        CBR存储库名称

        :param vault_name: The vault_name of this ResourceCopyItem.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceCopyItem.

        资源ID

        :return: The resource_id of this ResourceCopyItem.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceCopyItem.

        资源ID

        :param resource_id: The resource_id of this ResourceCopyItem.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ResourceCopyItem.

        资源名称

        :return: The resource_name of this ResourceCopyItem.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ResourceCopyItem.

        资源名称

        :param resource_name: The resource_name of this ResourceCopyItem.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, ResourceCopyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
