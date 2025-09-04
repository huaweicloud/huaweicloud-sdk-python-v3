# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestReportCustomDetailVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'name': 'str',
        'display': 'int',
        'description': 'str',
        'attachments': 'list[AttachmentVo]',
        'creator': 'str',
        'updator': 'str',
        'test_report_uri': 'str',
        'create_time': 'datetime',
        'create_timestamp': 'int',
        'creator_name': 'str',
        'update_time': 'datetime',
        'update_timestamp': 'int',
        'updator_name': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'display': 'display',
        'description': 'description',
        'attachments': 'attachments',
        'creator': 'creator',
        'updator': 'updator',
        'test_report_uri': 'test_report_uri',
        'create_time': 'create_time',
        'create_timestamp': 'create_timestamp',
        'creator_name': 'creator_name',
        'update_time': 'update_time',
        'update_timestamp': 'update_timestamp',
        'updator_name': 'updator_name'
    }

    def __init__(self, uri=None, name=None, display=None, description=None, attachments=None, creator=None, updator=None, test_report_uri=None, create_time=None, create_timestamp=None, creator_name=None, update_time=None, update_timestamp=None, updator_name=None):
        r"""TestReportCustomDetailVo

        The model defined in huaweicloud sdk

        :param uri: 测试报告自定义模块Uri
        :type uri: str
        :param name: 测试报告自定义模块名称
        :type name: str
        :param display: 是否显示(0:否，1:是)
        :type display: int
        :param description: 描述
        :type description: str
        :param attachments: 附件信息
        :type attachments: list[:class:`huaweicloudsdkcloudtest.v1.AttachmentVo`]
        :param creator: 创建人ID
        :type creator: str
        :param updator: 修改人ID
        :type updator: str
        :param test_report_uri: 测试报告uri
        :type test_report_uri: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param create_timestamp: 创建时间戳
        :type create_timestamp: int
        :param creator_name: 创建人名
        :type creator_name: str
        :param update_time: 修改时间
        :type update_time: datetime
        :param update_timestamp: 修改时间戳
        :type update_timestamp: int
        :param updator_name: 修改人名
        :type updator_name: str
        """
        
        

        self._uri = None
        self._name = None
        self._display = None
        self._description = None
        self._attachments = None
        self._creator = None
        self._updator = None
        self._test_report_uri = None
        self._create_time = None
        self._create_timestamp = None
        self._creator_name = None
        self._update_time = None
        self._update_timestamp = None
        self._updator_name = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if display is not None:
            self.display = display
        if description is not None:
            self.description = description
        if attachments is not None:
            self.attachments = attachments
        if creator is not None:
            self.creator = creator
        if updator is not None:
            self.updator = updator
        if test_report_uri is not None:
            self.test_report_uri = test_report_uri
        if create_time is not None:
            self.create_time = create_time
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if creator_name is not None:
            self.creator_name = creator_name
        if update_time is not None:
            self.update_time = update_time
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if updator_name is not None:
            self.updator_name = updator_name

    @property
    def uri(self):
        r"""Gets the uri of this TestReportCustomDetailVo.

        测试报告自定义模块Uri

        :return: The uri of this TestReportCustomDetailVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TestReportCustomDetailVo.

        测试报告自定义模块Uri

        :param uri: The uri of this TestReportCustomDetailVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def name(self):
        r"""Gets the name of this TestReportCustomDetailVo.

        测试报告自定义模块名称

        :return: The name of this TestReportCustomDetailVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TestReportCustomDetailVo.

        测试报告自定义模块名称

        :param name: The name of this TestReportCustomDetailVo.
        :type name: str
        """
        self._name = name

    @property
    def display(self):
        r"""Gets the display of this TestReportCustomDetailVo.

        是否显示(0:否，1:是)

        :return: The display of this TestReportCustomDetailVo.
        :rtype: int
        """
        return self._display

    @display.setter
    def display(self, display):
        r"""Sets the display of this TestReportCustomDetailVo.

        是否显示(0:否，1:是)

        :param display: The display of this TestReportCustomDetailVo.
        :type display: int
        """
        self._display = display

    @property
    def description(self):
        r"""Gets the description of this TestReportCustomDetailVo.

        描述

        :return: The description of this TestReportCustomDetailVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TestReportCustomDetailVo.

        描述

        :param description: The description of this TestReportCustomDetailVo.
        :type description: str
        """
        self._description = description

    @property
    def attachments(self):
        r"""Gets the attachments of this TestReportCustomDetailVo.

        附件信息

        :return: The attachments of this TestReportCustomDetailVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AttachmentVo`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        r"""Sets the attachments of this TestReportCustomDetailVo.

        附件信息

        :param attachments: The attachments of this TestReportCustomDetailVo.
        :type attachments: list[:class:`huaweicloudsdkcloudtest.v1.AttachmentVo`]
        """
        self._attachments = attachments

    @property
    def creator(self):
        r"""Gets the creator of this TestReportCustomDetailVo.

        创建人ID

        :return: The creator of this TestReportCustomDetailVo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this TestReportCustomDetailVo.

        创建人ID

        :param creator: The creator of this TestReportCustomDetailVo.
        :type creator: str
        """
        self._creator = creator

    @property
    def updator(self):
        r"""Gets the updator of this TestReportCustomDetailVo.

        修改人ID

        :return: The updator of this TestReportCustomDetailVo.
        :rtype: str
        """
        return self._updator

    @updator.setter
    def updator(self, updator):
        r"""Sets the updator of this TestReportCustomDetailVo.

        修改人ID

        :param updator: The updator of this TestReportCustomDetailVo.
        :type updator: str
        """
        self._updator = updator

    @property
    def test_report_uri(self):
        r"""Gets the test_report_uri of this TestReportCustomDetailVo.

        测试报告uri

        :return: The test_report_uri of this TestReportCustomDetailVo.
        :rtype: str
        """
        return self._test_report_uri

    @test_report_uri.setter
    def test_report_uri(self, test_report_uri):
        r"""Sets the test_report_uri of this TestReportCustomDetailVo.

        测试报告uri

        :param test_report_uri: The test_report_uri of this TestReportCustomDetailVo.
        :type test_report_uri: str
        """
        self._test_report_uri = test_report_uri

    @property
    def create_time(self):
        r"""Gets the create_time of this TestReportCustomDetailVo.

        创建时间

        :return: The create_time of this TestReportCustomDetailVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TestReportCustomDetailVo.

        创建时间

        :param create_time: The create_time of this TestReportCustomDetailVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_timestamp(self):
        r"""Gets the create_timestamp of this TestReportCustomDetailVo.

        创建时间戳

        :return: The create_timestamp of this TestReportCustomDetailVo.
        :rtype: int
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        r"""Sets the create_timestamp of this TestReportCustomDetailVo.

        创建时间戳

        :param create_timestamp: The create_timestamp of this TestReportCustomDetailVo.
        :type create_timestamp: int
        """
        self._create_timestamp = create_timestamp

    @property
    def creator_name(self):
        r"""Gets the creator_name of this TestReportCustomDetailVo.

        创建人名

        :return: The creator_name of this TestReportCustomDetailVo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this TestReportCustomDetailVo.

        创建人名

        :param creator_name: The creator_name of this TestReportCustomDetailVo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def update_time(self):
        r"""Gets the update_time of this TestReportCustomDetailVo.

        修改时间

        :return: The update_time of this TestReportCustomDetailVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TestReportCustomDetailVo.

        修改时间

        :param update_time: The update_time of this TestReportCustomDetailVo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this TestReportCustomDetailVo.

        修改时间戳

        :return: The update_timestamp of this TestReportCustomDetailVo.
        :rtype: int
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this TestReportCustomDetailVo.

        修改时间戳

        :param update_timestamp: The update_timestamp of this TestReportCustomDetailVo.
        :type update_timestamp: int
        """
        self._update_timestamp = update_timestamp

    @property
    def updator_name(self):
        r"""Gets the updator_name of this TestReportCustomDetailVo.

        修改人名

        :return: The updator_name of this TestReportCustomDetailVo.
        :rtype: str
        """
        return self._updator_name

    @updator_name.setter
    def updator_name(self, updator_name):
        r"""Sets the updator_name of this TestReportCustomDetailVo.

        修改人名

        :param updator_name: The updator_name of this TestReportCustomDetailVo.
        :type updator_name: str
        """
        self._updator_name = updator_name

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
        if not isinstance(other, TestReportCustomDetailVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
