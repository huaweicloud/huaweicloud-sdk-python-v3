# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnoseResourceVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fault': 'str',
        'id': 'str',
        'name': 'str',
        'access_i_pv4': 'str',
        'access_i_pv6': 'str',
        'status': 'str',
        'progress': 'str',
        'tenant_id': 'str',
        'user_id': 'str',
        'metadata': 'object',
        'host_id': 'str'
    }

    attribute_map = {
        'fault': 'fault',
        'id': 'id',
        'name': 'name',
        'access_i_pv4': 'accessIPv4',
        'access_i_pv6': 'accessIPv6',
        'status': 'status',
        'progress': 'progress',
        'tenant_id': 'tenantId',
        'user_id': 'userId',
        'metadata': 'metadata',
        'host_id': 'hostId'
    }

    def __init__(self, fault=None, id=None, name=None, access_i_pv4=None, access_i_pv6=None, status=None, progress=None, tenant_id=None, user_id=None, metadata=None, host_id=None):
        """DiagnoseResourceVo

        The model defined in huaweicloud sdk

        :param fault: ID 
        :type fault: str
        :param id: 状态
        :type id: str
        :param name: 名称
        :type name: str
        :param access_i_pv4: ip4地址
        :type access_i_pv4: str
        :param access_i_pv6: ip6地址
        :type access_i_pv6: str
        :param status: 状态
        :type status: str
        :param progress: 进度
        :type progress: str
        :param tenant_id: 前端id
        :type tenant_id: str
        :param user_id: 用户id
        :type user_id: str
        :param metadata: 资源元数据
        :type metadata: object
        :param host_id: 主机id
        :type host_id: str
        """
        
        

        self._fault = None
        self._id = None
        self._name = None
        self._access_i_pv4 = None
        self._access_i_pv6 = None
        self._status = None
        self._progress = None
        self._tenant_id = None
        self._user_id = None
        self._metadata = None
        self._host_id = None
        self.discriminator = None

        if fault is not None:
            self.fault = fault
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if access_i_pv4 is not None:
            self.access_i_pv4 = access_i_pv4
        if access_i_pv6 is not None:
            self.access_i_pv6 = access_i_pv6
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if user_id is not None:
            self.user_id = user_id
        if metadata is not None:
            self.metadata = metadata
        if host_id is not None:
            self.host_id = host_id

    @property
    def fault(self):
        """Gets the fault of this DiagnoseResourceVo.

        ID 

        :return: The fault of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        """Sets the fault of this DiagnoseResourceVo.

        ID 

        :param fault: The fault of this DiagnoseResourceVo.
        :type fault: str
        """
        self._fault = fault

    @property
    def id(self):
        """Gets the id of this DiagnoseResourceVo.

        状态

        :return: The id of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DiagnoseResourceVo.

        状态

        :param id: The id of this DiagnoseResourceVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DiagnoseResourceVo.

        名称

        :return: The name of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiagnoseResourceVo.

        名称

        :param name: The name of this DiagnoseResourceVo.
        :type name: str
        """
        self._name = name

    @property
    def access_i_pv4(self):
        """Gets the access_i_pv4 of this DiagnoseResourceVo.

        ip4地址

        :return: The access_i_pv4 of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._access_i_pv4

    @access_i_pv4.setter
    def access_i_pv4(self, access_i_pv4):
        """Sets the access_i_pv4 of this DiagnoseResourceVo.

        ip4地址

        :param access_i_pv4: The access_i_pv4 of this DiagnoseResourceVo.
        :type access_i_pv4: str
        """
        self._access_i_pv4 = access_i_pv4

    @property
    def access_i_pv6(self):
        """Gets the access_i_pv6 of this DiagnoseResourceVo.

        ip6地址

        :return: The access_i_pv6 of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._access_i_pv6

    @access_i_pv6.setter
    def access_i_pv6(self, access_i_pv6):
        """Sets the access_i_pv6 of this DiagnoseResourceVo.

        ip6地址

        :param access_i_pv6: The access_i_pv6 of this DiagnoseResourceVo.
        :type access_i_pv6: str
        """
        self._access_i_pv6 = access_i_pv6

    @property
    def status(self):
        """Gets the status of this DiagnoseResourceVo.

        状态

        :return: The status of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DiagnoseResourceVo.

        状态

        :param status: The status of this DiagnoseResourceVo.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        """Gets the progress of this DiagnoseResourceVo.

        进度

        :return: The progress of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DiagnoseResourceVo.

        进度

        :param progress: The progress of this DiagnoseResourceVo.
        :type progress: str
        """
        self._progress = progress

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DiagnoseResourceVo.

        前端id

        :return: The tenant_id of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DiagnoseResourceVo.

        前端id

        :param tenant_id: The tenant_id of this DiagnoseResourceVo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def user_id(self):
        """Gets the user_id of this DiagnoseResourceVo.

        用户id

        :return: The user_id of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DiagnoseResourceVo.

        用户id

        :param user_id: The user_id of this DiagnoseResourceVo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def metadata(self):
        """Gets the metadata of this DiagnoseResourceVo.

        资源元数据

        :return: The metadata of this DiagnoseResourceVo.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DiagnoseResourceVo.

        资源元数据

        :param metadata: The metadata of this DiagnoseResourceVo.
        :type metadata: object
        """
        self._metadata = metadata

    @property
    def host_id(self):
        """Gets the host_id of this DiagnoseResourceVo.

        主机id

        :return: The host_id of this DiagnoseResourceVo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this DiagnoseResourceVo.

        主机id

        :param host_id: The host_id of this DiagnoseResourceVo.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, DiagnoseResourceVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
