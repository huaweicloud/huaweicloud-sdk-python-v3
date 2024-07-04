# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIsolatedFileRequest:

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
        'file_path': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'file_hash': 'str',
        'asset_value': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'file_path': 'file_path',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'file_hash': 'file_hash',
        'asset_value': 'asset_value',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, region=None, enterprise_project_id=None, file_path=None, host_name=None, private_ip=None, public_ip=None, file_hash=None, asset_value=None, offset=None, limit=None):
        """ListIsolatedFileRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param file_path: 文件路径
        :type file_path: str
        :param host_name: 服务器名称
        :type host_name: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param file_hash: 文件hash,当前为sha256
        :type file_hash: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._file_path = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._file_hash = None
        self._asset_value = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if file_path is not None:
            self.file_path = file_path
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if file_hash is not None:
            self.file_hash = file_hash
        if asset_value is not None:
            self.asset_value = asset_value
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def region(self):
        """Gets the region of this ListIsolatedFileRequest.

        Region ID

        :return: The region of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListIsolatedFileRequest.

        Region ID

        :param region: The region of this ListIsolatedFileRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListIsolatedFileRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListIsolatedFileRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListIsolatedFileRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def file_path(self):
        """Gets the file_path of this ListIsolatedFileRequest.

        文件路径

        :return: The file_path of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this ListIsolatedFileRequest.

        文件路径

        :param file_path: The file_path of this ListIsolatedFileRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def host_name(self):
        """Gets the host_name of this ListIsolatedFileRequest.

        服务器名称

        :return: The host_name of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListIsolatedFileRequest.

        服务器名称

        :param host_name: The host_name of this ListIsolatedFileRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        """Gets the private_ip of this ListIsolatedFileRequest.

        服务器私有IP

        :return: The private_ip of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListIsolatedFileRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListIsolatedFileRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this ListIsolatedFileRequest.

        服务器公网IP

        :return: The public_ip of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ListIsolatedFileRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListIsolatedFileRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def file_hash(self):
        """Gets the file_hash of this ListIsolatedFileRequest.

        文件hash,当前为sha256

        :return: The file_hash of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        """Sets the file_hash of this ListIsolatedFileRequest.

        文件hash,当前为sha256

        :param file_hash: The file_hash of this ListIsolatedFileRequest.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def asset_value(self):
        """Gets the asset_value of this ListIsolatedFileRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        """Sets the asset_value of this ListIsolatedFileRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListIsolatedFileRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def offset(self):
        """Gets the offset of this ListIsolatedFileRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIsolatedFileRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListIsolatedFileRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIsolatedFileRequest.

        每页显示个数

        :return: The limit of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIsolatedFileRequest.

        每页显示个数

        :param limit: The limit of this ListIsolatedFileRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListIsolatedFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
