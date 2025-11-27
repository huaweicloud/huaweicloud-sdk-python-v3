# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReleaseParams:

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
        'replace': 'bool',
        'recreate': 'bool',
        'no_hooks': 'bool',
        'reset_values': 'bool',
        'name_template': 'str',
        'release_version': 'int',
        'include_hooks': 'bool'
    }

    attribute_map = {
        'dry_run': 'dry_run',
        'replace': 'replace',
        'recreate': 'recreate',
        'no_hooks': 'no_hooks',
        'reset_values': 'reset_values',
        'name_template': 'name_template',
        'release_version': 'release_version',
        'include_hooks': 'include_hooks'
    }

    def __init__(self, dry_run=None, replace=None, recreate=None, no_hooks=None, reset_values=None, name_template=None, release_version=None, include_hooks=None):
        r"""ReleaseParams

        The model defined in huaweicloud sdk

        :param dry_run: 是否仅模拟安装过程
        :type dry_run: bool
        :param replace: 是否允许重用已存在的名称
        :type replace: bool
        :param recreate: 是否强制重新创建资源
        :type recreate: bool
        :param no_hooks: 是否禁止hook
        :type no_hooks: bool
        :param reset_values: 更新时重设values
        :type reset_values: bool
        :param name_template: 发布资源的名称模板
        :type name_template: str
        :param release_version: 指定回滚版本号
        :type release_version: int
        :param include_hooks: 更新或删除时是否允许hook
        :type include_hooks: bool
        """
        
        

        self._dry_run = None
        self._replace = None
        self._recreate = None
        self._no_hooks = None
        self._reset_values = None
        self._name_template = None
        self._release_version = None
        self._include_hooks = None
        self.discriminator = None

        if dry_run is not None:
            self.dry_run = dry_run
        if replace is not None:
            self.replace = replace
        if recreate is not None:
            self.recreate = recreate
        if no_hooks is not None:
            self.no_hooks = no_hooks
        if reset_values is not None:
            self.reset_values = reset_values
        if name_template is not None:
            self.name_template = name_template
        if release_version is not None:
            self.release_version = release_version
        if include_hooks is not None:
            self.include_hooks = include_hooks

    @property
    def dry_run(self):
        r"""Gets the dry_run of this ReleaseParams.

        是否仅模拟安装过程

        :return: The dry_run of this ReleaseParams.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this ReleaseParams.

        是否仅模拟安装过程

        :param dry_run: The dry_run of this ReleaseParams.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def replace(self):
        r"""Gets the replace of this ReleaseParams.

        是否允许重用已存在的名称

        :return: The replace of this ReleaseParams.
        :rtype: bool
        """
        return self._replace

    @replace.setter
    def replace(self, replace):
        r"""Sets the replace of this ReleaseParams.

        是否允许重用已存在的名称

        :param replace: The replace of this ReleaseParams.
        :type replace: bool
        """
        self._replace = replace

    @property
    def recreate(self):
        r"""Gets the recreate of this ReleaseParams.

        是否强制重新创建资源

        :return: The recreate of this ReleaseParams.
        :rtype: bool
        """
        return self._recreate

    @recreate.setter
    def recreate(self, recreate):
        r"""Sets the recreate of this ReleaseParams.

        是否强制重新创建资源

        :param recreate: The recreate of this ReleaseParams.
        :type recreate: bool
        """
        self._recreate = recreate

    @property
    def no_hooks(self):
        r"""Gets the no_hooks of this ReleaseParams.

        是否禁止hook

        :return: The no_hooks of this ReleaseParams.
        :rtype: bool
        """
        return self._no_hooks

    @no_hooks.setter
    def no_hooks(self, no_hooks):
        r"""Sets the no_hooks of this ReleaseParams.

        是否禁止hook

        :param no_hooks: The no_hooks of this ReleaseParams.
        :type no_hooks: bool
        """
        self._no_hooks = no_hooks

    @property
    def reset_values(self):
        r"""Gets the reset_values of this ReleaseParams.

        更新时重设values

        :return: The reset_values of this ReleaseParams.
        :rtype: bool
        """
        return self._reset_values

    @reset_values.setter
    def reset_values(self, reset_values):
        r"""Sets the reset_values of this ReleaseParams.

        更新时重设values

        :param reset_values: The reset_values of this ReleaseParams.
        :type reset_values: bool
        """
        self._reset_values = reset_values

    @property
    def name_template(self):
        r"""Gets the name_template of this ReleaseParams.

        发布资源的名称模板

        :return: The name_template of this ReleaseParams.
        :rtype: str
        """
        return self._name_template

    @name_template.setter
    def name_template(self, name_template):
        r"""Sets the name_template of this ReleaseParams.

        发布资源的名称模板

        :param name_template: The name_template of this ReleaseParams.
        :type name_template: str
        """
        self._name_template = name_template

    @property
    def release_version(self):
        r"""Gets the release_version of this ReleaseParams.

        指定回滚版本号

        :return: The release_version of this ReleaseParams.
        :rtype: int
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        r"""Sets the release_version of this ReleaseParams.

        指定回滚版本号

        :param release_version: The release_version of this ReleaseParams.
        :type release_version: int
        """
        self._release_version = release_version

    @property
    def include_hooks(self):
        r"""Gets the include_hooks of this ReleaseParams.

        更新或删除时是否允许hook

        :return: The include_hooks of this ReleaseParams.
        :rtype: bool
        """
        return self._include_hooks

    @include_hooks.setter
    def include_hooks(self, include_hooks):
        r"""Sets the include_hooks of this ReleaseParams.

        更新或删除时是否允许hook

        :param include_hooks: The include_hooks of this ReleaseParams.
        :type include_hooks: bool
        """
        self._include_hooks = include_hooks

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
        if not isinstance(other, ReleaseParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
