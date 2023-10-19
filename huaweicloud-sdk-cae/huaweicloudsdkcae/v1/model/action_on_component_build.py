# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionOnComponentBuild:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'archive': 'Archive',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'archive': 'archive',
        'parameters': 'parameters'
    }

    def __init__(self, archive=None, parameters=None):
        """ActionOnComponentBuild

        The model defined in huaweicloud sdk

        :param archive: 
        :type archive: :class:`huaweicloudsdkcae.v1.Archive`
        :param parameters: 构建附加参数。 - base_image：基础镜像地址。 - build_cmd：自定义构建命令。 - dockerfile_path：自定义dockerfile文件路径 - dockerfile_content：自定义dockerfile内容 - artifact_name: 针对java多模块构建，指定构建后运行的产物，以\&quot;.jar\&quot;结尾。
        :type parameters: dict(str, str)
        """
        
        

        self._archive = None
        self._parameters = None
        self.discriminator = None

        if archive is not None:
            self.archive = archive
        if parameters is not None:
            self.parameters = parameters

    @property
    def archive(self):
        """Gets the archive of this ActionOnComponentBuild.

        :return: The archive of this ActionOnComponentBuild.
        :rtype: :class:`huaweicloudsdkcae.v1.Archive`
        """
        return self._archive

    @archive.setter
    def archive(self, archive):
        """Sets the archive of this ActionOnComponentBuild.

        :param archive: The archive of this ActionOnComponentBuild.
        :type archive: :class:`huaweicloudsdkcae.v1.Archive`
        """
        self._archive = archive

    @property
    def parameters(self):
        """Gets the parameters of this ActionOnComponentBuild.

        构建附加参数。 - base_image：基础镜像地址。 - build_cmd：自定义构建命令。 - dockerfile_path：自定义dockerfile文件路径 - dockerfile_content：自定义dockerfile内容 - artifact_name: 针对java多模块构建，指定构建后运行的产物，以\".jar\"结尾。

        :return: The parameters of this ActionOnComponentBuild.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ActionOnComponentBuild.

        构建附加参数。 - base_image：基础镜像地址。 - build_cmd：自定义构建命令。 - dockerfile_path：自定义dockerfile文件路径 - dockerfile_content：自定义dockerfile内容 - artifact_name: 针对java多模块构建，指定构建后运行的产物，以\".jar\"结尾。

        :param parameters: The parameters of this ActionOnComponentBuild.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

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
        if not isinstance(other, ActionOnComponentBuild):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
