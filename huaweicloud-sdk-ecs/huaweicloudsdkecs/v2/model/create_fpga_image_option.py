# coding: utf-8

import pprint
import re

import six


class CreateFpgaImageOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'dcp_location': 'str',
        'log_directory': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'dcp_location': 'dcp_location',
        'log_directory': 'log_directory',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, dcp_location=None, log_directory=None, name=None, description=None):  # noqa: E501
        """CreateFpgaImageOption - a model defined in huaweicloud sdk"""

        self._dcp_location = None
        self._log_directory = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.dcp_location = dcp_location
        if log_directory is not None:
            self.log_directory = log_directory
        self.name = name
        if description is not None:
            self.description = description

    @property
    def dcp_location(self):
        """Gets the dcp_location of this CreateFpgaImageOption.

        DCP文件在OBS桶中的路径，格式为“桶名:文件名”，例如“obs-fpga:fpga-test-dcp.tar”。  桶名的命名规则满足OBS的约束：  - 由英文小写字母、数字以及特殊字符“.”、“-”组成。  - 只能以数字或字母开头和结尾。  - 长度3～63个字符。  - 不能是ip地址。  - 不能包含“..”、“.-”&nbsp;、“-.”字符串。  文件名的命名规则如下：  - 由英文大、小写字母，数字，中划线，下划线，斜杠，英文句号组成。  - 不能以“/”开头。  - 必须以“.tar”结尾。  - 长度4～128个字符。  如果文件名中包含目录结构，例如“vu9p/fpga-test-dcp.tar”，则每一级目录名需要满足以下规则：  - 不能为空。  - 不能以“.”开头或结尾。

        :return: The dcp_location of this CreateFpgaImageOption.
        :rtype: str
        """
        return self._dcp_location

    @dcp_location.setter
    def dcp_location(self, dcp_location):
        """Sets the dcp_location of this CreateFpgaImageOption.

        DCP文件在OBS桶中的路径，格式为“桶名:文件名”，例如“obs-fpga:fpga-test-dcp.tar”。  桶名的命名规则满足OBS的约束：  - 由英文小写字母、数字以及特殊字符“.”、“-”组成。  - 只能以数字或字母开头和结尾。  - 长度3～63个字符。  - 不能是ip地址。  - 不能包含“..”、“.-”&nbsp;、“-.”字符串。  文件名的命名规则如下：  - 由英文大、小写字母，数字，中划线，下划线，斜杠，英文句号组成。  - 不能以“/”开头。  - 必须以“.tar”结尾。  - 长度4～128个字符。  如果文件名中包含目录结构，例如“vu9p/fpga-test-dcp.tar”，则每一级目录名需要满足以下规则：  - 不能为空。  - 不能以“.”开头或结尾。

        :param dcp_location: The dcp_location of this CreateFpgaImageOption.
        :type: str
        """
        self._dcp_location = dcp_location

    @property
    def log_directory(self):
        """Gets the log_directory of this CreateFpgaImageOption.

        构建日志文件在上传到OBS桶（DCP文件所在的OBS桶）中时的目录路径，例如“vu9p/log”。当该字段不存在或为空时，默认与用户的DCP文件位于同一级目录下。  命名规则如下：  - 由英文大、小写字母，数字，中划线，下划线，斜杠，英文句号组成。  - 不能以“/”开头或结尾。  - 如果包含多级目录，则每一级目录名都不能为空，且不能以“.”开头或结尾。  - 长度0～64个字符。

        :return: The log_directory of this CreateFpgaImageOption.
        :rtype: str
        """
        return self._log_directory

    @log_directory.setter
    def log_directory(self, log_directory):
        """Sets the log_directory of this CreateFpgaImageOption.

        构建日志文件在上传到OBS桶（DCP文件所在的OBS桶）中时的目录路径，例如“vu9p/log”。当该字段不存在或为空时，默认与用户的DCP文件位于同一级目录下。  命名规则如下：  - 由英文大、小写字母，数字，中划线，下划线，斜杠，英文句号组成。  - 不能以“/”开头或结尾。  - 如果包含多级目录，则每一级目录名都不能为空，且不能以“.”开头或结尾。  - 长度0～64个字符。

        :param log_directory: The log_directory of this CreateFpgaImageOption.
        :type: str
        """
        self._log_directory = log_directory

    @property
    def name(self):
        """Gets the name of this CreateFpgaImageOption.

        FPGA镜像的名称。  取值范围：  - 只能由英文字母、数字、下划线、中划线组成。  - 长度1~64个字符。

        :return: The name of this CreateFpgaImageOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFpgaImageOption.

        FPGA镜像的名称。  取值范围：  - 只能由英文字母、数字、下划线、中划线组成。  - 长度1~64个字符。

        :param name: The name of this CreateFpgaImageOption.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateFpgaImageOption.

        FPGA镜像的描述信息，由中文汉字、中文句号、中文逗号、英文大小写字母、数字、中划线、下划线、英文句号、英文逗号、空格组成，长度0到255个字符。

        :return: The description of this CreateFpgaImageOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateFpgaImageOption.

        FPGA镜像的描述信息，由中文汉字、中文句号、中文逗号、英文大小写字母、数字、中划线、下划线、英文句号、英文逗号、空格组成，长度0到255个字符。

        :param description: The description of this CreateFpgaImageOption.
        :type: str
        """
        self._description = description

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateFpgaImageOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
