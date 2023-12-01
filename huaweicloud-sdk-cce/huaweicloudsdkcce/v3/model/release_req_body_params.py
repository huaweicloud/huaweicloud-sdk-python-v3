# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReleaseReqBodyParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dry_run': 'bool',
        'name_template': 'str',
        'no_hooks': 'bool',
        'replace': 'bool',
        'recreate': 'bool',
        'reset_values': 'bool',
        'release_version': 'int',
        'include_hooks': 'bool'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'name_template': 'name_template',
        'no_hooks': 'no_hooks',
        'replace': 'replace',
        'recreate': 'recreate',
        'reset_values': 'reset_values',
        'release_version': 'release_version',
        'include_hooks': 'include_hooks'
    }

    def __init__(self, dry_run=None, name_template=None, no_hooks=None, replace=None, recreate=None, reset_values=None, release_version=None, include_hooks=None):
        """ReleaseReqBodyParams

        The model defined in huaweicloud sdk

        :param dry_run: 开启后，仅验证模板参数，不进行安装
        :type dry_run: bool
        :param name_template: 实例名称模板
        :type name_template: str
        :param no_hooks: 安装时是否禁用hooks
        :type no_hooks: bool
        :param replace: 是否替换同名实例
        :type replace: bool
        :param recreate: 是否重建实例
        :type recreate: bool
        :param reset_values: 更新时是否重置values
        :type reset_values: bool
        :param release_version: 回滚实例的版本
        :type release_version: int
        :param include_hooks: 更新或者删除时启用hooks
        :type include_hooks: bool
        """
        
        

        self._dry_run = None
        self._name_template = None
        self._no_hooks = None
        self._replace = None
        self._recreate = None
        self._reset_values = None
        self._release_version = None
        self._include_hooks = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        if name_template is not None:
            self.name_template = name_template
        if no_hooks is not None:
            self.no_hooks = no_hooks
        if replace is not None:
            self.replace = replace
        if recreate is not None:
            self.recreate = recreate
        if reset_values is not None:
            self.reset_values = reset_values
        if release_version is not None:
            self.release_version = release_version
        if include_hooks is not None:
            self.include_hooks = include_hooks

    @property
    def dry_run(self):
        """Gets the dry_run of this ReleaseReqBodyParams.

        开启后，仅验证模板参数，不进行安装

        :return: The dry_run of this ReleaseReqBodyParams.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ReleaseReqBodyParams.

        开启后，仅验证模板参数，不进行安装

        :param dry_run: The dry_run of this ReleaseReqBodyParams.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def name_template(self):
        """Gets the name_template of this ReleaseReqBodyParams.

        实例名称模板

        :return: The name_template of this ReleaseReqBodyParams.
        :rtype: str
        """
        return self._name_template

    @name_template.setter
    def name_template(self, name_template):
        """Sets the name_template of this ReleaseReqBodyParams.

        实例名称模板

        :param name_template: The name_template of this ReleaseReqBodyParams.
        :type name_template: str
        """
        self._name_template = name_template

    @property
    def no_hooks(self):
        """Gets the no_hooks of this ReleaseReqBodyParams.

        安装时是否禁用hooks

        :return: The no_hooks of this ReleaseReqBodyParams.
        :rtype: bool
        """
        return self._no_hooks

    @no_hooks.setter
    def no_hooks(self, no_hooks):
        """Sets the no_hooks of this ReleaseReqBodyParams.

        安装时是否禁用hooks

        :param no_hooks: The no_hooks of this ReleaseReqBodyParams.
        :type no_hooks: bool
        """
        self._no_hooks = no_hooks

    @property
    def replace(self):
        """Gets the replace of this ReleaseReqBodyParams.

        是否替换同名实例

        :return: The replace of this ReleaseReqBodyParams.
        :rtype: bool
        """
        return self._replace

    @replace.setter
    def replace(self, replace):
        """Sets the replace of this ReleaseReqBodyParams.

        是否替换同名实例

        :param replace: The replace of this ReleaseReqBodyParams.
        :type replace: bool
        """
        self._replace = replace

    @property
    def recreate(self):
        """Gets the recreate of this ReleaseReqBodyParams.

        是否重建实例

        :return: The recreate of this ReleaseReqBodyParams.
        :rtype: bool
        """
        return self._recreate

    @recreate.setter
    def recreate(self, recreate):
        """Sets the recreate of this ReleaseReqBodyParams.

        是否重建实例

        :param recreate: The recreate of this ReleaseReqBodyParams.
        :type recreate: bool
        """
        self._recreate = recreate

    @property
    def reset_values(self):
        """Gets the reset_values of this ReleaseReqBodyParams.

        更新时是否重置values

        :return: The reset_values of this ReleaseReqBodyParams.
        :rtype: bool
        """
        return self._reset_values

    @reset_values.setter
    def reset_values(self, reset_values):
        """Sets the reset_values of this ReleaseReqBodyParams.

        更新时是否重置values

        :param reset_values: The reset_values of this ReleaseReqBodyParams.
        :type reset_values: bool
        """
        self._reset_values = reset_values

    @property
    def release_version(self):
        """Gets the release_version of this ReleaseReqBodyParams.

        回滚实例的版本

        :return: The release_version of this ReleaseReqBodyParams.
        :rtype: int
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """Sets the release_version of this ReleaseReqBodyParams.

        回滚实例的版本

        :param release_version: The release_version of this ReleaseReqBodyParams.
        :type release_version: int
        """
        self._release_version = release_version

    @property
    def include_hooks(self):
        """Gets the include_hooks of this ReleaseReqBodyParams.

        更新或者删除时启用hooks

        :return: The include_hooks of this ReleaseReqBodyParams.
        :rtype: bool
        """
        return self._include_hooks

    @include_hooks.setter
    def include_hooks(self, include_hooks):
        """Sets the include_hooks of this ReleaseReqBodyParams.

        更新或者删除时启用hooks

        :param include_hooks: The include_hooks of this ReleaseReqBodyParams.
        :type include_hooks: bool
        """
        self._include_hooks = include_hooks

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
        if not isinstance(other, ReleaseReqBodyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
