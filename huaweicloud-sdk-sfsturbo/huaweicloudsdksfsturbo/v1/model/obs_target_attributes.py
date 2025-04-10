# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsTargetAttributes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_mode': 'int',
        'dir_mode': 'int',
        'uid': 'int',
        'gid': 'int'
    }

    attribute_map = {
        'file_mode': 'file_mode',
        'dir_mode': 'dir_mode',
        'uid': 'uid',
        'gid': 'gid'
    }

    def __init__(self, file_mode=None, dir_mode=None, uid=None, gid=None):
        r"""ObsTargetAttributes

        The model defined in huaweicloud sdk

        :param file_mode: 导入的文件权限。取值范围是0到777。  第一位表示文件所有者的权限，取值范围是0到7；第二位表示文件所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。文件所有者由uid指定，文件所属用户组由gid指定，不是文件所有者且不在文件所属用户组的用户为其他用户。  数字4、2、1分别表示读、写、执行权限，这些数字相加，即可得到所需的权限组合。例如：750中第一位7代表该文件所有者对该文件具有读、写、执行权限；第二位5代表该文件所属用户组对该文件具有读、执行权限；第三位0代表其他用户对该文件无权限。 
        :type file_mode: int
        :param dir_mode: 导入的目录权限。取值范围是0到777。  第一位表示目录所有者的权限，取值范围是0到7；第二位表示目录所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。目录所有者由uid指定，目录所属用户组由gid指定，不是目录所有者且不在目录所属用户组的用户为其他用户。  数字4、2、1分别表示读、写、执行权限，这些数字相加，即可得到所需的权限组合。例如：750中第一位7代表该目录所有者对该目录具有读、写、执行权限；第二位5代表该目录所属用户组对该目录具有读、执行权限；第三位0代表其他用户对该文件无权限。 
        :type dir_mode: int
        :param uid: 导入对象所有者的用户id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。
        :type uid: int
        :param gid: 导入对象所属用户组id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。
        :type gid: int
        """
        
        

        self._file_mode = None
        self._dir_mode = None
        self._uid = None
        self._gid = None
        self.discriminator = None

        if file_mode is not None:
            self.file_mode = file_mode
        if dir_mode is not None:
            self.dir_mode = dir_mode
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid

    @property
    def file_mode(self):
        r"""Gets the file_mode of this ObsTargetAttributes.

        导入的文件权限。取值范围是0到777。  第一位表示文件所有者的权限，取值范围是0到7；第二位表示文件所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。文件所有者由uid指定，文件所属用户组由gid指定，不是文件所有者且不在文件所属用户组的用户为其他用户。  数字4、2、1分别表示读、写、执行权限，这些数字相加，即可得到所需的权限组合。例如：750中第一位7代表该文件所有者对该文件具有读、写、执行权限；第二位5代表该文件所属用户组对该文件具有读、执行权限；第三位0代表其他用户对该文件无权限。 

        :return: The file_mode of this ObsTargetAttributes.
        :rtype: int
        """
        return self._file_mode

    @file_mode.setter
    def file_mode(self, file_mode):
        r"""Sets the file_mode of this ObsTargetAttributes.

        导入的文件权限。取值范围是0到777。  第一位表示文件所有者的权限，取值范围是0到7；第二位表示文件所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。文件所有者由uid指定，文件所属用户组由gid指定，不是文件所有者且不在文件所属用户组的用户为其他用户。  数字4、2、1分别表示读、写、执行权限，这些数字相加，即可得到所需的权限组合。例如：750中第一位7代表该文件所有者对该文件具有读、写、执行权限；第二位5代表该文件所属用户组对该文件具有读、执行权限；第三位0代表其他用户对该文件无权限。 

        :param file_mode: The file_mode of this ObsTargetAttributes.
        :type file_mode: int
        """
        self._file_mode = file_mode

    @property
    def dir_mode(self):
        r"""Gets the dir_mode of this ObsTargetAttributes.

        导入的目录权限。取值范围是0到777。  第一位表示目录所有者的权限，取值范围是0到7；第二位表示目录所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。目录所有者由uid指定，目录所属用户组由gid指定，不是目录所有者且不在目录所属用户组的用户为其他用户。  数字4、2、1分别表示读、写、执行权限，这些数字相加，即可得到所需的权限组合。例如：750中第一位7代表该目录所有者对该目录具有读、写、执行权限；第二位5代表该目录所属用户组对该目录具有读、执行权限；第三位0代表其他用户对该文件无权限。 

        :return: The dir_mode of this ObsTargetAttributes.
        :rtype: int
        """
        return self._dir_mode

    @dir_mode.setter
    def dir_mode(self, dir_mode):
        r"""Sets the dir_mode of this ObsTargetAttributes.

        导入的目录权限。取值范围是0到777。  第一位表示目录所有者的权限，取值范围是0到7；第二位表示目录所属用户组的权限，取值范围是0到7；第三位表示其他用户的权限，取值范围是0到7。目录所有者由uid指定，目录所属用户组由gid指定，不是目录所有者且不在目录所属用户组的用户为其他用户。  数字4、2、1分别表示读、写、执行权限，这些数字相加，即可得到所需的权限组合。例如：750中第一位7代表该目录所有者对该目录具有读、写、执行权限；第二位5代表该目录所属用户组对该目录具有读、执行权限；第三位0代表其他用户对该文件无权限。 

        :param dir_mode: The dir_mode of this ObsTargetAttributes.
        :type dir_mode: int
        """
        self._dir_mode = dir_mode

    @property
    def uid(self):
        r"""Gets the uid of this ObsTargetAttributes.

        导入对象所有者的用户id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。

        :return: The uid of this ObsTargetAttributes.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this ObsTargetAttributes.

        导入对象所有者的用户id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。

        :param uid: The uid of this ObsTargetAttributes.
        :type uid: int
        """
        self._uid = uid

    @property
    def gid(self):
        r"""Gets the gid of this ObsTargetAttributes.

        导入对象所属用户组id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。

        :return: The gid of this ObsTargetAttributes.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        r"""Sets the gid of this ObsTargetAttributes.

        导入对象所属用户组id，默认值是0，取值范围是0到4,294,967,294（即2^32-2）。

        :param gid: The gid of this ObsTargetAttributes.
        :type gid: int
        """
        self._gid = gid

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
        if not isinstance(other, ObsTargetAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
