# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamEnvironmentConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_agency_urn': 'str',
        'image_feature': 'str',
        'image_uri': 'str',
        'queue_name': 'str'
    }

    attribute_map = {
        'execution_agency_urn': 'execution_agency_urn',
        'image_feature': 'image_feature',
        'image_uri': 'image_uri',
        'queue_name': 'queue_name'
    }

    def __init__(self, execution_agency_urn=None, image_feature=None, image_uri=None, queue_name=None):
        """StreamEnvironmentConfig

        The model defined in huaweicloud sdk

        :param execution_agency_urn: 自定义委托名，定义作业级访问权限。
        :type execution_agency_urn: str
        :param image_feature: 表示用户作业使用的镜像类型。basic：表示使用 DLI 提供的基础镜像； custom：表示使用用户自定义的镜像。
        :type image_feature: str
        :param image_uri: 自定义镜像。当前只支持 SWR，格式为：组织名/镜像名:镜像版本。当用户设置“image_feature”为“custom”时，该参数生效。用户可通过与“image_feature”参数配合使用，指定作业运行使用自定义的镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。
        :type image_uri: str
        :param queue_name: 队列名称。长度限制：1-128个字符。
        :type queue_name: str
        """
        
        

        self._execution_agency_urn = None
        self._image_feature = None
        self._image_uri = None
        self._queue_name = None
        self.discriminator = None

        if execution_agency_urn is not None:
            self.execution_agency_urn = execution_agency_urn
        if image_feature is not None:
            self.image_feature = image_feature
        if image_uri is not None:
            self.image_uri = image_uri
        if queue_name is not None:
            self.queue_name = queue_name

    @property
    def execution_agency_urn(self):
        """Gets the execution_agency_urn of this StreamEnvironmentConfig.

        自定义委托名，定义作业级访问权限。

        :return: The execution_agency_urn of this StreamEnvironmentConfig.
        :rtype: str
        """
        return self._execution_agency_urn

    @execution_agency_urn.setter
    def execution_agency_urn(self, execution_agency_urn):
        """Sets the execution_agency_urn of this StreamEnvironmentConfig.

        自定义委托名，定义作业级访问权限。

        :param execution_agency_urn: The execution_agency_urn of this StreamEnvironmentConfig.
        :type execution_agency_urn: str
        """
        self._execution_agency_urn = execution_agency_urn

    @property
    def image_feature(self):
        """Gets the image_feature of this StreamEnvironmentConfig.

        表示用户作业使用的镜像类型。basic：表示使用 DLI 提供的基础镜像； custom：表示使用用户自定义的镜像。

        :return: The image_feature of this StreamEnvironmentConfig.
        :rtype: str
        """
        return self._image_feature

    @image_feature.setter
    def image_feature(self, image_feature):
        """Sets the image_feature of this StreamEnvironmentConfig.

        表示用户作业使用的镜像类型。basic：表示使用 DLI 提供的基础镜像； custom：表示使用用户自定义的镜像。

        :param image_feature: The image_feature of this StreamEnvironmentConfig.
        :type image_feature: str
        """
        self._image_feature = image_feature

    @property
    def image_uri(self):
        """Gets the image_uri of this StreamEnvironmentConfig.

        自定义镜像。当前只支持 SWR，格式为：组织名/镜像名:镜像版本。当用户设置“image_feature”为“custom”时，该参数生效。用户可通过与“image_feature”参数配合使用，指定作业运行使用自定义的镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。

        :return: The image_uri of this StreamEnvironmentConfig.
        :rtype: str
        """
        return self._image_uri

    @image_uri.setter
    def image_uri(self, image_uri):
        """Sets the image_uri of this StreamEnvironmentConfig.

        自定义镜像。当前只支持 SWR，格式为：组织名/镜像名:镜像版本。当用户设置“image_feature”为“custom”时，该参数生效。用户可通过与“image_feature”参数配合使用，指定作业运行使用自定义的镜像。关于如何使用自定义镜像，请参考《数据湖探索用户指南》。

        :param image_uri: The image_uri of this StreamEnvironmentConfig.
        :type image_uri: str
        """
        self._image_uri = image_uri

    @property
    def queue_name(self):
        """Gets the queue_name of this StreamEnvironmentConfig.

        队列名称。长度限制：1-128个字符。

        :return: The queue_name of this StreamEnvironmentConfig.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this StreamEnvironmentConfig.

        队列名称。长度限制：1-128个字符。

        :param queue_name: The queue_name of this StreamEnvironmentConfig.
        :type queue_name: str
        """
        self._queue_name = queue_name

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
        if not isinstance(other, StreamEnvironmentConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
