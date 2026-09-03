# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArtifactsPublish:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_ckpt': 'bool',
        'artifact_id': 'str',
        'asset_name': 'str',
        'visibility': 'str',
        'description': 'str',
        'publish_asset_type': 'str',
        'asset_source_type': 'str',
        'asset_code': 'str',
        'asset_version': 'str',
        'version_description': 'str'
    }

    attribute_map = {
        'is_ckpt': 'is_ckpt',
        'artifact_id': 'artifact_id',
        'asset_name': 'asset_name',
        'visibility': 'visibility',
        'description': 'description',
        'publish_asset_type': 'publish_asset_type',
        'asset_source_type': 'asset_source_type',
        'asset_code': 'asset_code',
        'asset_version': 'asset_version',
        'version_description': 'version_description'
    }

    def __init__(self, is_ckpt=None, artifact_id=None, asset_name=None, visibility=None, description=None, publish_asset_type=None, asset_source_type=None, asset_code=None, asset_version=None, version_description=None):
        r"""ArtifactsPublish

        The model defined in huaweicloud sdk

        :param is_ckpt: 是否是中间产物，false-是模型产物，true-是中间产物
        :type is_ckpt: bool
        :param artifact_id: 断点ID,ckpt发布时使用
        :type artifact_id: str
        :param asset_name: 模型产物发布后资产名称，默认{源模型名字}-{训练类型}-{训练时间}
        :type asset_name: str
        :param visibility: 全局可见性，用来控制资产是当前空间可见或者全部空间可见，取值current|all。
        :type visibility: str
        :param description: 发布资产描述信息，{任务名}的最终产出模型
        :type description: str
        :param publish_asset_type: 模型发布方式
        :type publish_asset_type: str
        :param asset_source_type: 资产来源
        :type asset_source_type: str
        :param asset_code: 选择模型。
        :type asset_code: str
        :param asset_version: 版本号。
        :type asset_version: str
        :param version_description: 版本描述。
        :type version_description: str
        """
        
        

        self._is_ckpt = None
        self._artifact_id = None
        self._asset_name = None
        self._visibility = None
        self._description = None
        self._publish_asset_type = None
        self._asset_source_type = None
        self._asset_code = None
        self._asset_version = None
        self._version_description = None
        self.discriminator = None

        if is_ckpt is not None:
            self.is_ckpt = is_ckpt
        if artifact_id is not None:
            self.artifact_id = artifact_id
        if asset_name is not None:
            self.asset_name = asset_name
        if visibility is not None:
            self.visibility = visibility
        if description is not None:
            self.description = description
        if publish_asset_type is not None:
            self.publish_asset_type = publish_asset_type
        if asset_source_type is not None:
            self.asset_source_type = asset_source_type
        if asset_code is not None:
            self.asset_code = asset_code
        if asset_version is not None:
            self.asset_version = asset_version
        if version_description is not None:
            self.version_description = version_description

    @property
    def is_ckpt(self):
        r"""Gets the is_ckpt of this ArtifactsPublish.

        是否是中间产物，false-是模型产物，true-是中间产物

        :return: The is_ckpt of this ArtifactsPublish.
        :rtype: bool
        """
        return self._is_ckpt

    @is_ckpt.setter
    def is_ckpt(self, is_ckpt):
        r"""Sets the is_ckpt of this ArtifactsPublish.

        是否是中间产物，false-是模型产物，true-是中间产物

        :param is_ckpt: The is_ckpt of this ArtifactsPublish.
        :type is_ckpt: bool
        """
        self._is_ckpt = is_ckpt

    @property
    def artifact_id(self):
        r"""Gets the artifact_id of this ArtifactsPublish.

        断点ID,ckpt发布时使用

        :return: The artifact_id of this ArtifactsPublish.
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        r"""Sets the artifact_id of this ArtifactsPublish.

        断点ID,ckpt发布时使用

        :param artifact_id: The artifact_id of this ArtifactsPublish.
        :type artifact_id: str
        """
        self._artifact_id = artifact_id

    @property
    def asset_name(self):
        r"""Gets the asset_name of this ArtifactsPublish.

        模型产物发布后资产名称，默认{源模型名字}-{训练类型}-{训练时间}

        :return: The asset_name of this ArtifactsPublish.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this ArtifactsPublish.

        模型产物发布后资产名称，默认{源模型名字}-{训练类型}-{训练时间}

        :param asset_name: The asset_name of this ArtifactsPublish.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def visibility(self):
        r"""Gets the visibility of this ArtifactsPublish.

        全局可见性，用来控制资产是当前空间可见或者全部空间可见，取值current|all。

        :return: The visibility of this ArtifactsPublish.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ArtifactsPublish.

        全局可见性，用来控制资产是当前空间可见或者全部空间可见，取值current|all。

        :param visibility: The visibility of this ArtifactsPublish.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def description(self):
        r"""Gets the description of this ArtifactsPublish.

        发布资产描述信息，{任务名}的最终产出模型

        :return: The description of this ArtifactsPublish.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ArtifactsPublish.

        发布资产描述信息，{任务名}的最终产出模型

        :param description: The description of this ArtifactsPublish.
        :type description: str
        """
        self._description = description

    @property
    def publish_asset_type(self):
        r"""Gets the publish_asset_type of this ArtifactsPublish.

        模型发布方式

        :return: The publish_asset_type of this ArtifactsPublish.
        :rtype: str
        """
        return self._publish_asset_type

    @publish_asset_type.setter
    def publish_asset_type(self, publish_asset_type):
        r"""Sets the publish_asset_type of this ArtifactsPublish.

        模型发布方式

        :param publish_asset_type: The publish_asset_type of this ArtifactsPublish.
        :type publish_asset_type: str
        """
        self._publish_asset_type = publish_asset_type

    @property
    def asset_source_type(self):
        r"""Gets the asset_source_type of this ArtifactsPublish.

        资产来源

        :return: The asset_source_type of this ArtifactsPublish.
        :rtype: str
        """
        return self._asset_source_type

    @asset_source_type.setter
    def asset_source_type(self, asset_source_type):
        r"""Sets the asset_source_type of this ArtifactsPublish.

        资产来源

        :param asset_source_type: The asset_source_type of this ArtifactsPublish.
        :type asset_source_type: str
        """
        self._asset_source_type = asset_source_type

    @property
    def asset_code(self):
        r"""Gets the asset_code of this ArtifactsPublish.

        选择模型。

        :return: The asset_code of this ArtifactsPublish.
        :rtype: str
        """
        return self._asset_code

    @asset_code.setter
    def asset_code(self, asset_code):
        r"""Sets the asset_code of this ArtifactsPublish.

        选择模型。

        :param asset_code: The asset_code of this ArtifactsPublish.
        :type asset_code: str
        """
        self._asset_code = asset_code

    @property
    def asset_version(self):
        r"""Gets the asset_version of this ArtifactsPublish.

        版本号。

        :return: The asset_version of this ArtifactsPublish.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        r"""Sets the asset_version of this ArtifactsPublish.

        版本号。

        :param asset_version: The asset_version of this ArtifactsPublish.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def version_description(self):
        r"""Gets the version_description of this ArtifactsPublish.

        版本描述。

        :return: The version_description of this ArtifactsPublish.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this ArtifactsPublish.

        版本描述。

        :param version_description: The version_description of this ArtifactsPublish.
        :type version_description: str
        """
        self._version_description = version_description

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
        if not isinstance(other, ArtifactsPublish):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
