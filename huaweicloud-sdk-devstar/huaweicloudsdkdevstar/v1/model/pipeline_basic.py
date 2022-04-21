# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineBasic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'id': 'str',
        'name': 'str',
        'url': 'str',
        'last_running_status': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'id': 'id',
        'name': 'name',
        'url': 'url',
        'last_running_status': 'last_running_status'
    }

    def __init__(self, uuid=None, id=None, name=None, url=None, last_running_status=None):
        """PipelineBasic

        The model defined in huaweicloud sdk

        :param uuid: DevStar系统生成的流水线UUID
        :type uuid: str
        :param id: CloudPipeline系统对应流水线ID
        :type id: str
        :param name: 流水线名称
        :type name: str
        :param url: 流水线地址
        :type url: str
        :param last_running_status: 流水线最后一次运行状态,success:成功,failed:失败,running:运行中
        :type last_running_status: str
        """
        
        

        self._uuid = None
        self._id = None
        self._name = None
        self._url = None
        self._last_running_status = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if last_running_status is not None:
            self.last_running_status = last_running_status

    @property
    def uuid(self):
        """Gets the uuid of this PipelineBasic.

        DevStar系统生成的流水线UUID

        :return: The uuid of this PipelineBasic.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this PipelineBasic.

        DevStar系统生成的流水线UUID

        :param uuid: The uuid of this PipelineBasic.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def id(self):
        """Gets the id of this PipelineBasic.

        CloudPipeline系统对应流水线ID

        :return: The id of this PipelineBasic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineBasic.

        CloudPipeline系统对应流水线ID

        :param id: The id of this PipelineBasic.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PipelineBasic.

        流水线名称

        :return: The name of this PipelineBasic.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineBasic.

        流水线名称

        :param name: The name of this PipelineBasic.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        """Gets the url of this PipelineBasic.

        流水线地址

        :return: The url of this PipelineBasic.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PipelineBasic.

        流水线地址

        :param url: The url of this PipelineBasic.
        :type url: str
        """
        self._url = url

    @property
    def last_running_status(self):
        """Gets the last_running_status of this PipelineBasic.

        流水线最后一次运行状态,success:成功,failed:失败,running:运行中

        :return: The last_running_status of this PipelineBasic.
        :rtype: str
        """
        return self._last_running_status

    @last_running_status.setter
    def last_running_status(self, last_running_status):
        """Sets the last_running_status of this PipelineBasic.

        流水线最后一次运行状态,success:成功,failed:失败,running:运行中

        :param last_running_status: The last_running_status of this PipelineBasic.
        :type last_running_status: str
        """
        self._last_running_status = last_running_status

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
        if not isinstance(other, PipelineBasic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
