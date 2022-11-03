# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'package_name': 'str',
        'file_size': 'int',
        'version_code': 'int',
        'min_sdk': 'str',
        'target_sdk': 'str',
        'sha1': 'str',
        'sha256': 'str',
        'md5': 'str',
        'issuer': 'str',
        'owner': 'str',
        'effective_date': 'str',
        'algorithm': 'str',
        'public_key': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'package_name': 'package_name',
        'file_size': 'file_size',
        'version_code': 'version_code',
        'min_sdk': 'min_sdk',
        'target_sdk': 'target_sdk',
        'sha1': 'sha1',
        'sha256': 'sha256',
        'md5': 'md5',
        'issuer': 'issuer',
        'owner': 'owner',
        'effective_date': 'effective_date',
        'algorithm': 'algorithm',
        'public_key': 'public_key'
    }

    def __init__(self, app_name=None, package_name=None, file_size=None, version_code=None, min_sdk=None, target_sdk=None, sha1=None, sha256=None, md5=None, issuer=None, owner=None, effective_date=None, algorithm=None, public_key=None):
        """BasicInfo

        The model defined in huaweicloud sdk

        :param app_name: 应用名称，移动应用特有
        :type app_name: str
        :param package_name: 文件包名
        :type package_name: str
        :param file_size: 文件大小
        :type file_size: int
        :param version_code: 版本号
        :type version_code: int
        :param min_sdk: 最小SDK版本
        :type min_sdk: str
        :param target_sdk: 目标SDK版本
        :type target_sdk: str
        :param sha1: 文件SHA1值
        :type sha1: str
        :param sha256: 文件SHA256值
        :type sha256: str
        :param md5: 文件MD5值
        :type md5: str
        :param issuer: 证书发布者
        :type issuer: str
        :param owner: 证书拥有者
        :type owner: str
        :param effective_date: 证书有效日期
        :type effective_date: str
        :param algorithm: 算法
        :type algorithm: str
        :param public_key: 证书公钥
        :type public_key: str
        """
        
        

        self._app_name = None
        self._package_name = None
        self._file_size = None
        self._version_code = None
        self._min_sdk = None
        self._target_sdk = None
        self._sha1 = None
        self._sha256 = None
        self._md5 = None
        self._issuer = None
        self._owner = None
        self._effective_date = None
        self._algorithm = None
        self._public_key = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if package_name is not None:
            self.package_name = package_name
        if file_size is not None:
            self.file_size = file_size
        if version_code is not None:
            self.version_code = version_code
        if min_sdk is not None:
            self.min_sdk = min_sdk
        if target_sdk is not None:
            self.target_sdk = target_sdk
        if sha1 is not None:
            self.sha1 = sha1
        if sha256 is not None:
            self.sha256 = sha256
        if md5 is not None:
            self.md5 = md5
        if issuer is not None:
            self.issuer = issuer
        if owner is not None:
            self.owner = owner
        if effective_date is not None:
            self.effective_date = effective_date
        if algorithm is not None:
            self.algorithm = algorithm
        if public_key is not None:
            self.public_key = public_key

    @property
    def app_name(self):
        """Gets the app_name of this BasicInfo.

        应用名称，移动应用特有

        :return: The app_name of this BasicInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this BasicInfo.

        应用名称，移动应用特有

        :param app_name: The app_name of this BasicInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def package_name(self):
        """Gets the package_name of this BasicInfo.

        文件包名

        :return: The package_name of this BasicInfo.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this BasicInfo.

        文件包名

        :param package_name: The package_name of this BasicInfo.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def file_size(self):
        """Gets the file_size of this BasicInfo.

        文件大小

        :return: The file_size of this BasicInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this BasicInfo.

        文件大小

        :param file_size: The file_size of this BasicInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def version_code(self):
        """Gets the version_code of this BasicInfo.

        版本号

        :return: The version_code of this BasicInfo.
        :rtype: int
        """
        return self._version_code

    @version_code.setter
    def version_code(self, version_code):
        """Sets the version_code of this BasicInfo.

        版本号

        :param version_code: The version_code of this BasicInfo.
        :type version_code: int
        """
        self._version_code = version_code

    @property
    def min_sdk(self):
        """Gets the min_sdk of this BasicInfo.

        最小SDK版本

        :return: The min_sdk of this BasicInfo.
        :rtype: str
        """
        return self._min_sdk

    @min_sdk.setter
    def min_sdk(self, min_sdk):
        """Sets the min_sdk of this BasicInfo.

        最小SDK版本

        :param min_sdk: The min_sdk of this BasicInfo.
        :type min_sdk: str
        """
        self._min_sdk = min_sdk

    @property
    def target_sdk(self):
        """Gets the target_sdk of this BasicInfo.

        目标SDK版本

        :return: The target_sdk of this BasicInfo.
        :rtype: str
        """
        return self._target_sdk

    @target_sdk.setter
    def target_sdk(self, target_sdk):
        """Sets the target_sdk of this BasicInfo.

        目标SDK版本

        :param target_sdk: The target_sdk of this BasicInfo.
        :type target_sdk: str
        """
        self._target_sdk = target_sdk

    @property
    def sha1(self):
        """Gets the sha1 of this BasicInfo.

        文件SHA1值

        :return: The sha1 of this BasicInfo.
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this BasicInfo.

        文件SHA1值

        :param sha1: The sha1 of this BasicInfo.
        :type sha1: str
        """
        self._sha1 = sha1

    @property
    def sha256(self):
        """Gets the sha256 of this BasicInfo.

        文件SHA256值

        :return: The sha256 of this BasicInfo.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this BasicInfo.

        文件SHA256值

        :param sha256: The sha256 of this BasicInfo.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def md5(self):
        """Gets the md5 of this BasicInfo.

        文件MD5值

        :return: The md5 of this BasicInfo.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this BasicInfo.

        文件MD5值

        :param md5: The md5 of this BasicInfo.
        :type md5: str
        """
        self._md5 = md5

    @property
    def issuer(self):
        """Gets the issuer of this BasicInfo.

        证书发布者

        :return: The issuer of this BasicInfo.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this BasicInfo.

        证书发布者

        :param issuer: The issuer of this BasicInfo.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def owner(self):
        """Gets the owner of this BasicInfo.

        证书拥有者

        :return: The owner of this BasicInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BasicInfo.

        证书拥有者

        :param owner: The owner of this BasicInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def effective_date(self):
        """Gets the effective_date of this BasicInfo.

        证书有效日期

        :return: The effective_date of this BasicInfo.
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this BasicInfo.

        证书有效日期

        :param effective_date: The effective_date of this BasicInfo.
        :type effective_date: str
        """
        self._effective_date = effective_date

    @property
    def algorithm(self):
        """Gets the algorithm of this BasicInfo.

        算法

        :return: The algorithm of this BasicInfo.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this BasicInfo.

        算法

        :param algorithm: The algorithm of this BasicInfo.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def public_key(self):
        """Gets the public_key of this BasicInfo.

        证书公钥

        :return: The public_key of this BasicInfo.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this BasicInfo.

        证书公钥

        :param public_key: The public_key of this BasicInfo.
        :type public_key: str
        """
        self._public_key = public_key

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
        if not isinstance(other, BasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
