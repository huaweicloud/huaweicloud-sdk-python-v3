# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'datastore': 'Datastore',
        'availability_zone': 'str',
        'nics': 'list[Nic]',
        'cluster_info': 'CreateClusterReqBodyClusterInfo',
        'enterprise_project_id': 'str',
        'vpc_id': 'str',
        'dbuser': 'str',
        'dbuserpwd': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'datastore': 'datastore',
        'availability_zone': 'availability_zone',
        'nics': 'nics',
        'cluster_info': 'cluster_info',
        'enterprise_project_id': 'enterprise_project_id',
        'vpc_id': 'vpc_id',
        'dbuser': 'dbuser',
        'dbuserpwd': 'dbuserpwd'
    }

    def __init__(self, cluster_name=None, datastore=None, availability_zone=None, nics=None, cluster_info=None, enterprise_project_id=None, vpc_id=None, dbuser=None, dbuserpwd=None):
        """CreateClusterReqBody

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名字
        :type cluster_name: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        :param availability_zone: 可用区
        :type availability_zone: str
        :param nics: 集群所在的网络信息以及安全组信息。
        :type nics: list[:class:`huaweicloudsdkcloudtable.v2.Nic`]
        :param cluster_info: 
        :type cluster_info: :class:`huaweicloudsdkcloudtable.v2.CreateClusterReqBodyClusterInfo`
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param vpc_id: 虚拟私有云ID
        :type vpc_id: str
        :param dbuser: type为doris时，必填项，管理账号：admin
        :type dbuser: str
        :param dbuserpwd: type为doris时，必填项，管理账号密码
        :type dbuserpwd: str
        """
        
        

        self._cluster_name = None
        self._datastore = None
        self._availability_zone = None
        self._nics = None
        self._cluster_info = None
        self._enterprise_project_id = None
        self._vpc_id = None
        self._dbuser = None
        self._dbuserpwd = None
        self.discriminator = None

        self.cluster_name = cluster_name
        self.datastore = datastore
        self.availability_zone = availability_zone
        self.nics = nics
        self.cluster_info = cluster_info
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.vpc_id = vpc_id
        if dbuser is not None:
            self.dbuser = dbuser
        if dbuserpwd is not None:
            self.dbuserpwd = dbuserpwd

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateClusterReqBody.

        集群名字

        :return: The cluster_name of this CreateClusterReqBody.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateClusterReqBody.

        集群名字

        :param cluster_name: The cluster_name of this CreateClusterReqBody.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def datastore(self):
        """Gets the datastore of this CreateClusterReqBody.

        :return: The datastore of this CreateClusterReqBody.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateClusterReqBody.

        :param datastore: The datastore of this CreateClusterReqBody.
        :type datastore: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        """
        self._datastore = datastore

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateClusterReqBody.

        可用区

        :return: The availability_zone of this CreateClusterReqBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateClusterReqBody.

        可用区

        :param availability_zone: The availability_zone of this CreateClusterReqBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def nics(self):
        """Gets the nics of this CreateClusterReqBody.

        集群所在的网络信息以及安全组信息。

        :return: The nics of this CreateClusterReqBody.
        :rtype: list[:class:`huaweicloudsdkcloudtable.v2.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CreateClusterReqBody.

        集群所在的网络信息以及安全组信息。

        :param nics: The nics of this CreateClusterReqBody.
        :type nics: list[:class:`huaweicloudsdkcloudtable.v2.Nic`]
        """
        self._nics = nics

    @property
    def cluster_info(self):
        """Gets the cluster_info of this CreateClusterReqBody.

        :return: The cluster_info of this CreateClusterReqBody.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.CreateClusterReqBodyClusterInfo`
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        """Sets the cluster_info of this CreateClusterReqBody.

        :param cluster_info: The cluster_info of this CreateClusterReqBody.
        :type cluster_info: :class:`huaweicloudsdkcloudtable.v2.CreateClusterReqBodyClusterInfo`
        """
        self._cluster_info = cluster_info

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateClusterReqBody.

        企业项目ID

        :return: The enterprise_project_id of this CreateClusterReqBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateClusterReqBody.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this CreateClusterReqBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateClusterReqBody.

        虚拟私有云ID

        :return: The vpc_id of this CreateClusterReqBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateClusterReqBody.

        虚拟私有云ID

        :param vpc_id: The vpc_id of this CreateClusterReqBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def dbuser(self):
        """Gets the dbuser of this CreateClusterReqBody.

        type为doris时，必填项，管理账号：admin

        :return: The dbuser of this CreateClusterReqBody.
        :rtype: str
        """
        return self._dbuser

    @dbuser.setter
    def dbuser(self, dbuser):
        """Sets the dbuser of this CreateClusterReqBody.

        type为doris时，必填项，管理账号：admin

        :param dbuser: The dbuser of this CreateClusterReqBody.
        :type dbuser: str
        """
        self._dbuser = dbuser

    @property
    def dbuserpwd(self):
        """Gets the dbuserpwd of this CreateClusterReqBody.

        type为doris时，必填项，管理账号密码

        :return: The dbuserpwd of this CreateClusterReqBody.
        :rtype: str
        """
        return self._dbuserpwd

    @dbuserpwd.setter
    def dbuserpwd(self, dbuserpwd):
        """Sets the dbuserpwd of this CreateClusterReqBody.

        type为doris时，必填项，管理账号密码

        :param dbuserpwd: The dbuserpwd of this CreateClusterReqBody.
        :type dbuserpwd: str
        """
        self._dbuserpwd = dbuserpwd

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
        if not isinstance(other, CreateClusterReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
