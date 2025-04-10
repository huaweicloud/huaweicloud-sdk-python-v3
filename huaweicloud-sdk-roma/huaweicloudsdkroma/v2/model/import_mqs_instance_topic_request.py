# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportMqsInstanceTopicRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'mode': 'str',
        'prefix': 'str',
        'body': 'ImportMqsInstanceTopicRequestBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'mode': 'mode',
        'prefix': 'prefix',
        'body': 'body'
    }

    def __init__(self, instance_id=None, mode=None, prefix=None, body=None):
        r"""ImportMqsInstanceTopicRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param mode: 导入topic的模式。 - AddNew：全量新增导入。 - Merge：合并导入。  默认为AddNew模式。
        :type mode: str
        :param prefix: App应用的前缀。  若加上前缀，导入Topic时会拼接前缀和已有的App应用，形成新的App应用名称，再根据新的App应用名称导入Topic。
        :type prefix: str
        :param body: Body of the ImportMqsInstanceTopicRequest
        :type body: :class:`huaweicloudsdkroma.v2.ImportMqsInstanceTopicRequestBody`
        """
        
        

        self._instance_id = None
        self._mode = None
        self._prefix = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        if mode is not None:
            self.mode = mode
        if prefix is not None:
            self.prefix = prefix
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ImportMqsInstanceTopicRequest.

        实例ID。

        :return: The instance_id of this ImportMqsInstanceTopicRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ImportMqsInstanceTopicRequest.

        实例ID。

        :param instance_id: The instance_id of this ImportMqsInstanceTopicRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def mode(self):
        r"""Gets the mode of this ImportMqsInstanceTopicRequest.

        导入topic的模式。 - AddNew：全量新增导入。 - Merge：合并导入。  默认为AddNew模式。

        :return: The mode of this ImportMqsInstanceTopicRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ImportMqsInstanceTopicRequest.

        导入topic的模式。 - AddNew：全量新增导入。 - Merge：合并导入。  默认为AddNew模式。

        :param mode: The mode of this ImportMqsInstanceTopicRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def prefix(self):
        r"""Gets the prefix of this ImportMqsInstanceTopicRequest.

        App应用的前缀。  若加上前缀，导入Topic时会拼接前缀和已有的App应用，形成新的App应用名称，再根据新的App应用名称导入Topic。

        :return: The prefix of this ImportMqsInstanceTopicRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ImportMqsInstanceTopicRequest.

        App应用的前缀。  若加上前缀，导入Topic时会拼接前缀和已有的App应用，形成新的App应用名称，再根据新的App应用名称导入Topic。

        :param prefix: The prefix of this ImportMqsInstanceTopicRequest.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def body(self):
        r"""Gets the body of this ImportMqsInstanceTopicRequest.

        :return: The body of this ImportMqsInstanceTopicRequest.
        :rtype: :class:`huaweicloudsdkroma.v2.ImportMqsInstanceTopicRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ImportMqsInstanceTopicRequest.

        :param body: The body of this ImportMqsInstanceTopicRequest.
        :type body: :class:`huaweicloudsdkroma.v2.ImportMqsInstanceTopicRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ImportMqsInstanceTopicRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
